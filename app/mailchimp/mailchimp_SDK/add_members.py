from mailchimp_marketing.api_client import ApiClientError
from app.mockapi.mockapi import fetch_contacts
from app.utils import get_client_list_id

def add_members():
    members = fetch_contacts()
    new_members = get_members_info(members)
    response = get_response_add(new_members)
    return response

def get_members_info(members):
    new_members = []
    for member in members:
        if "email" in member and "firstName" in member and "lastName" in member:
            filtered_member_info = {
                "email_address": member["email"],
                "status": "subscribed",
                "email_type": "text",
                "merge_fields": {
                    "FNAME": member["firstName"],
                    "LNAME": member["lastName"]
                }
            }
            new_members.append(filtered_member_info)
    return new_members
    
def get_response_add(new_members):
    client, list_id = get_client_list_id()
    try:
        response = client.lists.batch_list_members(list_id, {"members": new_members})
    except ApiClientError as error:
        print("Mailchimp API Error:")
        print("Status code:", error.status_code)
        print("Full message:", error.text)
        print("Error details:", error)
        return {"error": error.text}
    return response