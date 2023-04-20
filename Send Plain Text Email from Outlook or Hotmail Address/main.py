import smtplib

sender = 'pypy08555@outlook.com'

receiver = "wckqurzg@drope.ml"
password = "Python2467"

message = """\
Subject: Hello Hello

This is SHarim!
Just wanted to greet you!
"""

server = smtplib.SMTP('smtp.office365.com', 995)
server.starttls()
server.login(user=sender, password=password)
server.sendmail(sender, receiver, message)
server.quit()
print("done")