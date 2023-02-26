import ssl
from email.message import EmailMessage
import ssl
import smtplib


email_sender='praveen9703970690@gmail.com'
email_password='oymblumaatrguksn'
email_receiver='praveen9703970690@gmail.com'

subject='hi'
body="""
Hi this is first email using python ..
it will be succeeded...

"""
em=EmailMessage()
em['From']=email_sender
em['To']=email_sender
em['Subject']=subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())


