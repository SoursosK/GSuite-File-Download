import requests
from datetime import date

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTw3bKwBT9JCiuW5vIR2EhBGh12dJOnszH0PQN0r8Bvb0jnfurYfzo4Pmmk1aIct_WH5kR9BDK56H_7/pub?output=pdf"  # you can get the whole link in the 'Publish to the web' dialog
r = requests.get(url)
with open( str(date.today()) + '.pdf', 'wb') as f:
    f.write(r.content)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "your@domain.com"
toaddr = "target@domain.gr"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Email Subject Title"

# string to store the body of the mail
body = "Email Body"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = str(date.today()) + '.pdf'
attachment = open("file path", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.domain.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "password")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
