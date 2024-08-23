import smtplib
import ssl
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import threading


sender = 'NA'
receiver = 'NA'
password = 'TOKEN'  # Note: APP PASSOWRD IN GOOGLE
subject = 'Test Email with Photo Attachment'
body = "YO WAHTS UP" #message


photo_path = 'quest.png'  # Photo path or photo with the script


context = ssl.create_default_context()


msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject


msg.attach(MIMEText(body, 'plain'))


try:
    with open(photo_path, 'rb') as attachment:
        img = MIMEImage(attachment.read(), name='hahaha.png')
        msg.attach(img)
except Exception as e:
    print(f"Could not open or attach the photo: {e}")


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
