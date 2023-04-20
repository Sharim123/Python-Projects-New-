import yagmail
import pandas

sender = "pypy08555@gmail.com"

subject = "This is the subject!"

password = "xkdqxbawtmsbwmrw"

yag = yagmail.SMTP(user=sender, password=password)

df = pandas.read_csv("contacts.csv")

def generate_file(filename, content):
    with open(f'{filename}.txt', 'w') as file:
        file.write(str(content))


for index, row in df.iterrows():
    name = row["name"]
    amount = row['amount']
    receiver_email = row['email']
    generate_file(name, amount)


    content = [f'Hey, {name} you have to pay {amount}. Bill is attached!', f"{name}.txt"]
    yag.send(to=receiver_email, subject=subject, contents=content)
    print("Email Sent!")