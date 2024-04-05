import datetime
from twilio.rest import Client

account_sid = 'ACa3ded3cd0b39b0efe288198c34e401de'
auth_token = '5047729895bfaeea2b9f3ad01051640f'
client = Client(account_sid, auth_token)

date = datetime.datetime.now().date()
inpm = datetime.datetime.now().time()

message = client.messages.create(
  from_='+19893680649',
  body=f'LRN number:xxxx entered on {date} {inpm}',
  to='+639456678590'
)

print(message.body)