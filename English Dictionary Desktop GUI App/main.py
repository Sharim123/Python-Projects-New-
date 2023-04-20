from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QLabel
import json


with open("data.json") as f:
    dict = json.load(f)


def search():
    input = text.text()
    input = input.lower()
    if input in dict:
        definition = dict[f'{input}']
        message.setText(f'{definition}')
    else:
        def refresh():



        message.setText("Output does not exist. Please double check.")
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(refresh)
        layout1.addWidget(refresh_button)







app = QApplication([])

window = QWidget()
window.setWindowTitle("Word Definition")
layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

text = QLineEdit()
layout1.addWidget(text)

search_button = QPushButton("Convert")
search_button.clicked.connect(search)
layout1.addWidget(search_button)

message = QLabel()
layout.addWidget(message)

window.setLayout(layout)
window.show()
app.exec()