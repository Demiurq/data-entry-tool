from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QGridLayout, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QKeyEvent
import sys
import os
import pandas as pd

if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv")
    print(df)
if not os.path.exists("data.csv"):
    with open("data.csv", "w") as file:
        file.write("data,value" + "\n")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Entry Tool")
        self.setMinimumSize(400, 200)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        self.input_text = QLineEdit()
        layout.addWidget(self.input_text, 0, 0)

        submit = QPushButton("Submit")
        submit.clicked.connect(self.submit)
        layout.addWidget(submit, 1, 0)

    def keyPressEvent(self, event: QKeyEvent):
        super().keyPressEvent(event)

        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.submit()

    def submit(self):
        text = self.input_text.text()
        text = text.replace(" ", ",")
        with open("data.csv", "a+") as f:
            f.writelines(text + "\n")
        self.input_text.setText("")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

