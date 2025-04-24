import os
import mailchimp_marketing as MailchimpMarketing

def get_client_list_id():
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": os.getenv("MAILCHIMP_API_KEY"),
        "server": os.getenv("MAILCHIMP_PREFIX")
    }) 
    
    list_id = os.getenv("LIST_ID")
    
    return client, list_id