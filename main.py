from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "AC620182553450bc48eb090595ce69e4d2"
auth_token  = "b023dfd3722a1a41d735a88fc6eef538"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+32479407776",
    from_="+12566009835",
    body="Hello eva here!")

print(message.sid)