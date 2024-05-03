from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACCOUNT_SID"
auth_token  = "AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="receving_phone_number",
    from_="+12566009835",
    body="Hello eva here!")

print(message.sid)
