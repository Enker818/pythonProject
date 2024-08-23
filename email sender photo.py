import smtplib
import ssl
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import threading

# Define sender and receiver email addresses
sender = 'NA'
receiver = 'NA'
password = 'TOKEN'  # Note: Replace with a valid app-specific password or manage it securely
subject = 'Test Email with Photo Attachment'
body = "YO WAHTS UP"

# Path to the photo you want to attach
photo_path = 'quest.png'  # Change this to the actual path of your photo

# Create a secure SSL context
context = ssl.create_default_context()

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject

# Attach the body with MIMEText
msg.attach(MIMEText(body, 'plain'))

# Attach the photo
try:
    with open(photo_path, 'rb') as attachment:
        img = MIMEImage(attachment.read(), name='hahaha.png')
        msg.attach(img)
except Exception as e:
    print(f"Could not open or attach the photo: {e}")

# Function to send the email
def send_email():
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("Email sent successfully!")
            return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

# Attempt to send the email in a loop until successful

def lol():
    while True:
        send_email()

threads = []

for i in range(20):
    t = threading.Thread(target=lol)
    t.daemon = True
    threads.append(t)


for i in range(20):
    threads[i].start()

for i in range(20):
    threads[i].join()
