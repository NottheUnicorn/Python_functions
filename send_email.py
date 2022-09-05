import smtplib

sender_email = 'walshrjoseph@gmail.com'
sender_password = 'Spring2017'

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject,body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)