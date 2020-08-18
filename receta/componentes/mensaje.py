import smtplib

# import the corresponding modules
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

clavecorreosender = 'CRRBCRRBCRRBCRRB1978'

class Email_HE1(object):
    def __init__(self, subject, sender_email, receiver_email, body, filename, smtpservidor, port, password):
        self.subject = subject
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.body = body
        self.filename = filename
        self.smtpservidor = smtpservidor
        self.port = port
        self.password = password

    def enviar_mensaje(self):
        subject = self.subject
        sender_email = self.sender_email
        receiver_email = self.receiver_email

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add body to email
        body = self.body
        message.attach(MIMEText(body, "plain"))

        filename = self.filename
        # Open PDF file in binary mode

        # We assume that the file is in the directory where you run your Python script from
        with open(filename, "rb") as attachment:
            # The content type "application/octet-stream" means that a MIME attachment is a binary file
            part = MIMEBase("application", "pdf")
            part.set_payload(attachment.read())

        # Encode to base64
        encoders.encode_base64(part)

        # Add header
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to your message and convert it to string
        message.attach(part)
        text = message.as_string()

        # send your email
        # with smtplib.SMTP("localhost", 25) as server:
        with smtplib.SMTP(self.smtpservidor, port=self.port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.sender_email, self.password)
            server.sendmail(sender_email, receiver_email, text)
