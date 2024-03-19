import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Gopal Gurram'
email['to'] = 'gopalgurram1@gmail.com'
email['Subject'] = 'You have won a 1M USD!'

email.set_content('I am a python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('temp@gmail.com', '')
    smtp.send_message(email)
    print('All Good Let\'s Go')
