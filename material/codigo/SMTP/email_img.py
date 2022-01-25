from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com" # Gmail SMTP host address
port = 587 # TLS port

# Email data
sender = "graphycrypto8@gmail.com"
receiver = "tareasydesarrollo@gmail.com"
pswd = "Usuario123_"

conn = smtplib.SMTP(host, port)
conn.starttls()
conn.login(sender, pswd)

subject = "Ciberseguridad pista 2"

message = MIMEMultipart()
message['from'] = "Tu mero chile"
message['to'] = receiver
message['subject'] = subject

# Email text
message.attach(MIMEText('Ta potente esa madre', 'plain'))

# Email message
image = open("T2.png", "rb").read()
message.attach(MIMEImage(image, name="Pista2.png"))

conn.sendmail(sender, receiver, message.as_string())

conn.quit()