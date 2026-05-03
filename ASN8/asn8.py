import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Submit.clicked.connect(self.displayData)
        self.ui.Reset.clicked.connect(self.clearFields)
        self.ui.Quit.clicked.connect(self.close)

    def displayData(self):
        first = self.ui.FirstName.text().strip()
        last = self.ui.LastName.text().strip()
        email = self.ui.Email_2.text().strip()
        phone = self.ui.PhoneNumber.text().strip()

        if first == "" or last == "":
            QMessageBox.warning(
                self,
                "Error",
                "First Name and Last Name are required."
            )
            return

        output = (
            f"First Name: {first}\n"
            f"Last Name: {last}\n"
            f"Email: {email}\n"
            f"Phone: {phone}"
        )

        QMessageBox.information(
            self,
            "Submitted Information",
            output
        )

    def clearFields(self):
        self.ui.FirstName.clear()
        self.ui.LastName.clear()
        self.ui.Email_2.clear()
        self.ui.PhoneNumber.clear()
        self.ui.FirstName.setFocus()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()