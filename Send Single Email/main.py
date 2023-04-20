import yagmail

sender = 'pypy08555@gmail.com'
receiver = "a48se8a0@flymail.tk"

subject = "This is the subject"

content = "This is the content of the email"
password = "xkdqxbawtmsbwmrw"

yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=content)

print("done")