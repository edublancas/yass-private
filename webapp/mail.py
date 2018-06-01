import smtplib


def send(subject, body):
    sender = 'eduardo@loki'
    receivers = ['fkq8@blancas.io']

    message = """From: From Person <eduardo@loki>
    To: To Person <fkq8@blancas.io>
    Subject: {}

    {}
    """.format(subject, body)

    smtp_obj = smtplib.SMTP('localhost')
    smtp_obj.sendmail(sender, receivers, message)
