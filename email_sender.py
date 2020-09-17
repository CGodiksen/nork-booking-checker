from __future__ import print_function

import base64
import os.path
import pickle
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class EmailSender:
    def __init__(self, sender, receiver):
        """
        :param sender: Email address of the sender.
        :param receiver: Email address of the receiver.
        """
        self.sender = sender
        self.receiver = receiver

        # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

        self.service = None
        self.__get_gmail_service()

    def send_conflict_email(self, double_bookings):
        """Creates and sends an email to the specified receiver notifying them about one or more double bookings."""

    def __get_gmail_service(self):
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
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run.
            with open('token.pickle', 'wb') as token:
                pickle.dump(credentials, token)

        self.service = build('gmail', 'v1', credentials=credentials)

    def __create_message(self, subject, message_text):
        """Create a message for an email.

        :param subject: The subject of the email message.
        :param message_text: The text of the email message.
        :return: An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = self.receiver
        message['from'] = self.sender
        message['subject'] = subject

        b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
        b64_string = b64_bytes.decode()
        return {'raw': b64_string}

    def __send_message(self, user_id, message):
        """Send an email message.

        :param user_id: User's email address. The special value "me" can be used to indicate the authenticated user.
        :param message: Message to be sent.
        :return: Sent Message.
        """
        try:
            message = (self.service.users().messages().send(userId=user_id, body=message).execute())
            print('Message Id: %s' % message['id'])
            return message
        except HttpError as error:
            print('An error occurred: %s' % error)

