'''
A simple python script to send 
notifications to your personal
email

author: GotoCode
'''

import smtplib


# user credentials
username = '???'
pwd      = '???'

from_addr = '???'
to_addr   = '???'


# message to send
msg = 'YOUR MESSAGE HERE!'


# connect to SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)

# initiate TLS encryption
server.starttls()

# login to the SMTP server
server.login(username, pwd)

# send simple plain-text email
server.sendmail(from_addr, to_addr, msg)

# terminate SMTP session
server.quit()