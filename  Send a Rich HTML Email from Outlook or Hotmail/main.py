import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

sender = 'pypy08555@outlook.com'

receiver = "wckqurzg@drope.ml"
password = "Python2467"

message = """\
Subject: Hello Hello

This is SHarim!
Just wanted to greet you!
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
