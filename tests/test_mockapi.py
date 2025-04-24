from app.mockapi.mockapi import fetch_contacts
import httpx

def test_fetch_contacts_success(mocker):
    mock_get = mocker.patch("httpx.Client.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"email": "a@b.com", "firstName": "A", "lastName": "B"}]

    result = fetch_contacts()
    assert isinstance(result, list)
    assert result[0]["email"] == "a@b.com"

def test_fetch_contacts_network_error(mocker):
    mocker.patch("httpx.Client.get", side_effect=httpx.RequestError("Network failure"))
    result = fetch_contacts()
    assert result == []




