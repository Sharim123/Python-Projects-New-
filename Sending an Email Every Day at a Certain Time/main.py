import yagmail
import time
from datetime import datetime as dt

sender = 'pypy08555@gmail.com'
receiver = "a48se8a0@flymail.tk"

subject = "This is the subject"

content = "This is the content of the email"
password = "xkdqxbawtmsbwmrw"


while True:
    now = dt.now()
    if now.hour == 15 and now.minute == 55:
        yag = yagmail.SMTP(user=sender, password=password)
        yag.send(to=receiver, subject=subject, contents=content)
        print("done")
        time.sleep(60)