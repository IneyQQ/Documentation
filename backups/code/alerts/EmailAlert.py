from coreinterfaces.alert import Alert
import smtplib
from email.mime.text import MIMEText


class EmailAlert(Alert):
    smtp_host = "mail.iba"

    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def alert(self, theme, message):
        smtp = smtplib.SMTP(EmailAlert.smtp_host)
        msg = MIMEText(message)
        msg['Subject'] = theme
        msg['From'] = self.sender
        msg['To'] = self.recipient
        smtp.send_message(msg)
        smtp.close()
