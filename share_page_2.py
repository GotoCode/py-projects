'''
A simple python script to send 
notifications to your personal
email

author: GotoCode
'''

import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# user credentials
username = '???'
pwd      = '???'

from_addr = '???'
to_addr   = '???'


# email headers
headers = MIMEMultipart()

headers['From']    = from_addr
headers['To']      = to_addr
headers['Subject'] = 'SUBJECT'


# message to send
msg = 'YOUR MESSAGE HERE!'
headers.attach(MIMEText(msg))


# connect to SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)

# initiate TLS encryption
server.starttls()

# login to the SMTP server
server.login(username, pwd)

# send simple plain-text email
server.sendmail(from_addr, to_addr, headers.as_string())

# terminate SMTP session
server.quit()