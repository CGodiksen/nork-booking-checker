import smtplib
import ssl


class Email:
    def __init__(self):
        self.port = 465  # For SSL.

        self.password = None
        self.email = None

        # Create a secure SSL context.
        self.context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.email, self.password)
