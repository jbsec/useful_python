import smtplib
sender_mail = input("Enter your gmail address:")
receivers_mail = input("Enter recipents gmail:")
message = """From: Person %s
To: To Person %s
Subject: Sending SMTP e-mail
This is a test e-mail message.
"""%(sender_mail,receivers_mail)
try:
    password = input ('Enter the password: ');
    smtp0bj = smtpblib.SMTP('gmail.com'587)
    smtp0bj.login(sender_mail,password)
    smtp0bj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully send email")
except Exception:
    print("Error: unable to send email")