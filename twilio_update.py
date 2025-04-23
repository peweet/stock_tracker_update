from dotenv import load_dotenv
from twilio.rest import Client
import os
load_dotenv()
class TwilioSMS:
    def __init__(self):
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    def sms_message(self, input_body):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
        body=(f"Stock has dramatically shifted. TESLA articles to read: {input_body}"),
        from_=os.environ['TWILIO_FROM_NUMBER'],
        to=os.environ['TWILIO_TO_NUMBER'],
        )
        print(f"Test the service: {message.body}")