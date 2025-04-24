import json
import pytest
from flask import Response
from unittest.mock import MagicMock
from app.mailchimp.mailchimp_SDK.add_members import get_members_info, get_response_add
from app.mailchimp.mailchimp_SDK.retrieve_members import retrieve_contacts, get_response_retrieve
from app.mailchimp.mailchimp_SDK.utils import parse_mailchimp_contacts

def test_get_members_info_filters_valid_contacts():
    input_data = [
        {"email": "valid@example.com", "firstName": "John", "lastName": "Doe"},
        {"email": "invalid@example.com", "firstName": "OnlyFirst"},
        {"lastName": "OnlyLast", "email": "no_first@example.com"}
    ]
    
    result = get_members_info(input_data)
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["email_address"] == "valid@example.com"
    

def test_get_response_add_api_error(mocker):
    from mailchimp_marketing.api_client import ApiClientError

    mock_client = MagicMock()
    error = ApiClientError(status_code=400, text="API error")
    mock_client.lists.batch_list_members.side_effect = error

    mocker.patch("app.utils.get_client_list_id", return_value=(mock_client, "fake-list-id"))

    response = get_response_add([])
    assert "error" in response
    
    
def test_retrieve_contacts_returns_valid_response(mocker):
    mocker.patch("app.mailchimp.mailchimp_SDK.retrieve_members.get_response_retrieve", return_value={
        "members": [
            {"email_address": "test@mail.com", "merge_fields": {"FNAME": "Test", "LNAME": "User"}}
        ]
    })

    response = retrieve_contacts()
    assert isinstance(response, Response)
    
    data = json.loads(response.data)
    assert data["syncedContacts"] == 1
    assert data["contacts"][0]["email"] == "test@mail.com"    


def test_get_response_retrieve_api_error(mocker):
    from mailchimp_marketing.api_client import ApiClientError

    mock_client = MagicMock()
    mock_client.lists.get_list_members_info.side_effect = ApiClientError(status_code=401, text="Unauthorized")
    mocker.patch("app.utils.get_client_list_id", return_value=(mock_client, "list-id"))

    result = get_response_retrieve()
    assert "error" in result or isinstance(result, str)
    
    
def test_parse_mailchimp_contacts_filters_fields():
    raw = [
        {
            "email_address": "a@mail.com",
            "merge_fields": {
                "FNAME": "Alice",
                "LNAME": "Wonderland"
            }
        },
        {
            "email_address": "b@mail.com",
            "merge_fields": {}
        }
    ]
    result = parse_mailchimp_contacts(raw)
    assert len(result) == 1
    assert result[0]["email"] == "a@mail.com"