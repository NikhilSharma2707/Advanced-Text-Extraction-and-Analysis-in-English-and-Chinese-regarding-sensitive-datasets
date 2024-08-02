import os
from mailjet_rest import Client
import base64
import random
import string

# Function to generate random info for the subject
def generate_random_subject():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Function to send an email with QR code attachment using Mailjet
def send_email(to_email, subject, body, qr_code_path):
    api_key = '2c2b20eeacbf1a37daaa060078f744f4'
    api_secret = '58059d6ad13503de57c5e4a467befa51'

    # Read the QR code file
    with open(qr_code_path, 'rb') as f:
        qr_code_data = f.read()

    # Encode the QR code file as base64
    qr_code_base64 = base64.b64encode(qr_code_data).decode()

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "moodoxyy@gmail.com",
                    "Name": "Nikhil Sharma"
                },
                "To": [
                    {
                        "Email": to_email,
                        "Name": "Recipient"
                    }
                ],
                "Subject": subject,
                "TextPart": body,
                "Attachments": [
                    {
                        "ContentType": "image/png",
                        "Filename": os.path.basename(qr_code_path),
                        "Base64Content": qr_code_base64
                    }
                ]
            }
        ]
    }

    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

if __name__ == "__main__":
    # Specific user and QR code
    recipient_email = "adityaprinshu2004@gmail.com"
    qr_code_path = r"C:\MW\QR\qr_code_1.png"

    subject = "Your QR Code - " + generate_random_subject()
    body = "Please find your QR code attached."

    send_email(recipient_email, subject, body, qr_code_path)
