import smtplib
import ssl



sender = 'ibrayimtari@gmail.com'
taker = 'ankerahet@gmail.com'
password = 'jzdk qezq llvv ixgn'
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

