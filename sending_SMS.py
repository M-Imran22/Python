
from twilio.rest import Client
import os

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello it's imran using python script to send you this message.",
    from_='+1 507 687 6525',
    to='+923005860312'
)

print("Message sent with SID: ", message.sid)
