import smtplib
import ssl
import json


class Email:
    def __init__(self):
        self.port = 465  # For SSL.

        self.email = None
        self.password = None
        self.__retrieve_email_password()

        # Create a secure SSL context.
        self.context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.email, self.password)

    def __retrieve_email_password(self):
        """Retrieves the email and password from the "email_config.json" file and updates the class attributes."""
        with open("email_config.json", "r") as email_config:
            config_dict = json.load(email_config)

            self.email = config_dict["email"]
            self.password = config_dict["password"]


test = Email()