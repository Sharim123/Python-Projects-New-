import yagmail
import pandas

sender = 'pypy08555@gmail.com'


subject = "This is the subject"

password = "xkdqxbawtmsbwmrw"

yag = yagmail.SMTP(user=sender, password=password)

df = pandas.read_csv("contacts.csv")
# print(df)

for index, row in df.iterrows():
    content = f'Hi {row["name"]} the content of the email'
    yag.send(to=row['email'], subject=subject, contents=content)
    print("done")
