import smtplib
import email.utils
from email.mime.text import MIMEText


def send(subject, body):
    sender = 'eduardo@loki'
    receivers = ['fkq8@blancas.io']

    msg = MIMEText(body)
    msg['To'] = email.utils.formataddr(('Eduardo', 'fkq8@blancas.io'))
    msg['From'] = email.utils.formataddr(('eduado@loki', 'eduardo@loki'))
    msg['Subject'] = subject

    smtp_obj = smtplib.SMTP('localhost')
    smtp_obj.sendmail(sender, receivers, msg.as_string())
