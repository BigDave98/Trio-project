from mailchimp_marketing.api_client import ApiClientError
from app.mockapi.mockapi import fetch_contacts
from app.utils import get_client_list_id

def add_members():    
  members = fetch_contacts()  
  new_members = get_members_info(members)

  response = get_response(new_members)

  return response

def get_members_info(members):
  new_members = []
  for member in members:
    if "email" in member and "firstName" in member and "lastName" in member:   
      filtered_member_info = {"email_address": member["email"],
                              "status": "subscribed",
                              "email_type": "text",
                              "merge_fields": {
                                "FNAME": member["firstName"],
                                "LNAME": member["lastName"]
                              }                    
                            }    
      
      new_members.append(filtered_member_info)
  return new_members
    
def get_response(new_members):  
  client, list_id = get_client_list_id()
  
  try:
      response = client.lists.batch_list_members(list_id, {"members": new_members})
  except ApiClientError as error:
      print("Erro da API Mailchimp:")
      print("Status code:", error.status_code)  # Exibe o código do erro (se disponível)
      print("Mensagem completa:", error.text)  # Exibe a mensagem completa de erro
      print("Detalhes do erro:", error)  # Exibe a exceção completa, com mais detalhes (inclui traceback)
      return {"error": error.text}  # Retorna a mensagem de erro
  
  return response