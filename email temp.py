import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import time

# Email sender and receiver
sender_email = "NA"  # Replace with your email
receiver_email = "NA"  # Replace with recipient's email
password = "token"  # Replace with your email password or app-specific password

# Email subject and body
subject = "Test Email"
body = "This is a test email sent from a Python script."

# Create a secure SSL context
context = ssl.create_default_context()

# Create the email message
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

# Send email in a loop with a delay
for _ in range(10):  # Adjust the range as needed
    if send_email():
        time.sleep(1)  # Wait for 1 second before sending the next email
    else:
        break
