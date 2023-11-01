from twilio.rest import Client

TWILIO_SID = "AC86d66c02e728246f0a60ff1088dd7087"
TWILIO_AUTH_TOKEN = "8c73a24c6e7f62256be1bd86e4eefdc4"
TWILIO_VIRTUAL_NUMBER = "+14179892752"
TWILIO_VERIFIED_NUMBER = "+919076450014"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
