from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import pyperclip

class PasswordManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.setFixedSize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        # Create widgets
        self.website_label = QLabel("Website:")
        self.website_entry = QLineEdit()
        self.email_label = QLabel("Email/Username:")
        self.email_entry = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_password)

        # Create layout
        form_layout = QFormLayout()
        form_layout.addRow(self.website_label, self.website_entry)
        form_layout.addRow(self.email_label, self.email_entry)
        form_layout.addRow(self.password_label, self.password_entry)
        form_layout.addRow(self.generate_button)
        form_layout.addRow(self.save_button)

        # Create central widget
        central_widget = QWidget()
        central_widget.setLayout(form_layout)
        self.setCentralWidget(central_widget)

    def generate_password(self):
        """Function to generate a random password"""
        password_length = 12
        password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
        password = "".join(random.choice(password_chars) for i in range(password_length))
        self.password_entry.setText(password)

    def save_password(self):
        """Function to save the password and related information to a file"""
        website = self.website_entry.text()
        email = self.email_entry.text()
        password = self.password_entry.text()

        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        self.website_entry.setText("")
        self.email_entry.setText("")
        self.password_entry.setText("")
        QMessageBox.information(self, "Success", "Password saved successfully!")
        pyperclip.copy(password)

if __name__ == '__main__':
    app = QApplication([])
    password_manager = PasswordManager()
    password_manager.show()
    app.exec_()
