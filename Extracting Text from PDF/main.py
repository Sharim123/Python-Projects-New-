import fitz



with fitz.open('students.pdf') as pdf:
    text = ''
    for page in pdf:
        print(text + page.get_text())
