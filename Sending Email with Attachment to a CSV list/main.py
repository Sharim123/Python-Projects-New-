import yagmail
import pandas

sender = "pypy08555@gmail.com"

subject = "This is the subject!"

password = "xkdqxbawtmsbwmrw"

yag = yagmail.SMTP(user=sender, password=password)

df = pandas.read_csv("contacts.csv")

for index, row in df:
    content = [f'Hey, {row["name"]} you have to pay {row["amount"]}\n Bill is attached!', f"{row['filepath']}"]
    yag.send(to=row['email'], subject=subject, contents=content)

