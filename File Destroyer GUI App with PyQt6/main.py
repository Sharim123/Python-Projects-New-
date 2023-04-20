from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


def browse():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select Files")
    message.setText('\n'.join(filenames))

def destroy():
    for filename in filenames:
        path = Path(filename)
        with open(path, "wb") as file:
            file.write(b'')
        path.unlink()
    message.setText('Destruction Successful')


app = QApplication([])

window = QWidget()
window.setWindowTitle("File Destroyer")
layout = QVBoxLayout()

text = QLabel("Select the files you want to destroy. The files will be <font color='red'>permanently</font> deleted")
layout.addWidget(text)

btn1 = QPushButton("Open Files")
btn1.setToolTip("Open")
btn1.setFixedWidth(100)
btn1.clicked.connect(browse)
layout.addWidget(btn1, alignment=Qt.AlignmentFlag.AlignCenter)

btn2 = QPushButton("Destroy Files")
btn2.setFixedWidth(100)
btn2.setToolTip("Destroy")
layout.addWidget(btn2, alignment=Qt.AlignmentFlag.AlignCenter)

btn2.clicked.connect(destroy)

message = QLabel()
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()