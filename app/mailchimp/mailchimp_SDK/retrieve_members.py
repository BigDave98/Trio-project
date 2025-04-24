import json

from collections import OrderedDict
from flask import Response
from mailchimp_marketing.api_client import ApiClientError
from app.mailchimp.mailchimp_SDK.utils import parse_mailchimp_contacts
from app.utils import get_client_list_id


def retrieve_contacts():
  response = get_response()
      
  members = response.get("members", '')
  parsed_response = parse_mailchimp_contacts(members)
  number_contacts = len(parsed_response)
  
  output = OrderedDict()
  output["syncedContacts"] = number_contacts
  output["contacts"] = parsed_response

    
  return Response(
        response=json.dumps(output, indent=2),
        status=200,
        mimetype="application/json"
  )
  
def get_response():
  client, list_id = get_client_list_id()
  count = 1000
  
  try:
        response = client.lists.get_list_members_info(list_id, count=count)
        
  except ApiClientError as error:
        print("Erro ao recuperar contatos:", error.text)
        return []
  
  return response
      
