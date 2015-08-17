from twilio.rest import TwilioRestClient
from twilio_secret import *



client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


# this is the command to send a text number from your twillio number to the to number with the message of body.
message=client.messages.create(from_=TWILLIO_NUMBER, to=to_number, body="Hello! This is rosy, this is myself")

# when it sends a message, it will make a unique id. This is going to tell you if it did something or not.
print message.sid 