
import json
import requests

phone_number_id = "115767534727567" # Phone number ID provided
access_token = "EAAWs5STvFN4BAHa59Wj1zE5eVP29CoF6oQVmMEVNhc7JP2MkDvBq8VZAUEsbbhq2FyXaujUfZAOZBNnKRY6IPDm1dIPSMahPqmKAIX1CRoVRZAka3Fs2yaYQ4LRUt2bN9rVVCTVPEINa2hd7zIyDtscEeSIuYvZCrIfnJZCwLosoSZBuPQZALJzCNmCGiv80V5bnp59rsGHsKXwJpz1846hw4Yy2krXguBYZD"
recipient_phone_number = "+256787364702" # Your own phone number


url = "https://graph.facebook.com/v15.0/115767534727567/messages"
headers = {
    "Authorization": f"Bearer {access_token}",
    'Content-Type': 'application/json'
}


data = { 
"messaging_product": "whatsapp", 
"to": recipient_phone_number, 
"type": "template", 
"template": { 
    "name": "hello_world", 
    "language": { 
        "code": "en_US" 
        } 
    } 
}

response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data)
    )

print(response)
# otp_code = '3424'
# driver_name = 'David'

# msg_body_params = [
#         {
#             "type": "text",
#             "text": otp_code
#         },
#         {
#             "type": "text",
#             "text": driver_name
#         }
# ]


# data = {
#     'messaging_product': 'whatsapp',
#     'to': recipient_phone_number,
#     'type': 'template',
#     'template': {
#         'name': 'hello_world',
#         'language': {
#             'code': 'en'
#         },
#         # 'components': [
#         #     {
#         #         'type': 'body',
#         #         'parameters': msg_body_params
#         #     }
                
#         # ]
#     }
# }


# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hello there!',
#                               from_='whatsapp:+14155238886',
#                               to='whatsapp:+15005550006'
#                           )

# print(message.sid)