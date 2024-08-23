import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import time


sender_email = "NA"
receiver_email = "NA"
password = "token"


subject = "Test Email"
body = "This is a test email sent from a Python script."


context = ssl.create_default_context()


msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

def send_email():
    try:
        print("Connecting to the server...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.set_debuglevel(1)  # Enable verbose output
            print("Connected.")
            server.login(sender_email, password)
            print("Logged in successfully.")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
            return True
    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Please check your email and password.")
    except smtplib.SMTPConnectError:
        print("Connection error: Unable to connect to the SMTP server.")
    except smtplib.SMTPServerDisconnected:
        print("Server unexpectedly disconnected.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False


for _ in range(10):
    if send_email():
        time.sleep(1)
    else:
        break
