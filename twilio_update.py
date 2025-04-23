from dotenv import load_dotenv
from twilio.rest import Client
import os
load_dotenv()
class TwilioSMS:
    def __init__(self):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]

    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

    def sms_message(self, input_body):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
        body=(f"Stock has dramatically shifted. TESLA articles to read: {input_body}"),
        from_=os.environ['TWILIO_FROM_NUMBER'],
        to=os.environ['TWILIO_TO_NUMBER'],
        )
        print(f"Test the service: {message.body}")