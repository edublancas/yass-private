import smtplib


def send():
    sender = 'eduardo@loki'
    receivers = ['fkq8@blancas.io']

    message = """From: From Person <eduardo@loki>
    To: To Person <fkq8@blancas.io>
    Subject: Peformance test done

    Performance testing finished running
    """

    smtp_obj = smtplib.SMTP('localhost')
    smtp_obj.sendmail(sender, receivers, message)
