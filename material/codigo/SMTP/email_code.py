import smtplib
import getpass


host = "smtp.gmail.com" # Gmail SMTP host address
port = 587 # TLS port

# Email data
sender = "graphycrypto8@gmail.com"
receiver = "tareasydesarrollo@gmail.com"
pswd = "Usuario123_"
message = "Hello, my dear lirul prins"

# Starting the connection to the port
conn = smtplib.SMTP(host, port)
# Identify us a in the server
conn.ehlo()
# Generate a TLS encryption required for the port
conn.starttls()
# Send the credentials to the server
conn.login(user=sender, password=pswd)

conn.sendmail(sender, receiver, message)

conn.quit()
