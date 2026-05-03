import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Assignment 6")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Directions label
        self.lblHelp = QLabel("Enter an integer greater than 2")
        self.lblHelp.setAlignment(Qt.AlignCenter)
        self.lblHelp.setStyleSheet("background-color: #DCEEF2; padding: 8px;")

        # Input box
        self.input = QLineEdit()
        self.input.setAlignment(Qt.AlignCenter)

        # Output label
        self.lblOutput = QLabel("Your random number will appear here")
        self.lblOutput.setAlignment(Qt.AlignCenter)
        self.lblOutput.setFont(QFont("Arial", 25))
        self.lblOutput.setStyleSheet("background-color: #E8F5E9; padding: 12px;")
        # Random Number Button
        self.btnRand = QPushButton("Random Numbers")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.lblHelp)
        layout.addWidget(self.input)
        layout.addWidget(self.lblOutput)
        layout.addWidget(self.btnRand)

        central_widget.setLayout(layout)

        self.btnRand.clicked.connect(self.update_label)

    def update_label(self):
        text_value = self.input.text()

        try:
            user_num = int(text_value)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a proper integer.")
            self.input.clear()
            self.lblOutput.setText("")
            return

        if user_num < 2:
            QMessageBox.warning(self, "Invalid Input", "Please enter an integer greater than 2.")
            self.input.clear()
            self.lblOutput.setText("")
            return

        rand_num = random.randint(1, user_num)
        self.lblOutput.setText(str(rand_num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())