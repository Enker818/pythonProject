import smtplib
import ssl



sender = 'email'
taker = 
password = 'your token'
subject = 'test'
body = """
YO WAHTS UP
"""

em = "HAHHA"

con = ssl.create_default_context()
while True:
 with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=con) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,taker, em)
    print("email sendt")

