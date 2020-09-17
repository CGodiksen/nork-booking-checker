from __future__ import print_function

import base64
import os.path
import pickle
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class EmailSender:
    def __init__(self):
        # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

        self.service = None
        self.get_gmail_service()

    def get_gmail_service(self):
        credentials = None
        # The file token.pickle stores the user's access and refresh tokens, and is created automatically when the
        # authorization flow completes for the first time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                credentials = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run.
            with open('token.pickle', 'wb') as token:
                pickle.dump(credentials, token)

        self.service = build('gmail', 'v1', credentials=credentials)

    @staticmethod
    def create_message(sender, to, subject, message_text):
        """Create a message for an email.

        :param sender: Email address of the sender.
        :param to: Email address of the receiver.
        :param subject: The subject of the email message.
        :param message_text: The text of the email message.
        :return: An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject

        return {'raw': base64.urlsafe_b64encode(message.as_string())}


test = EmailSender()
