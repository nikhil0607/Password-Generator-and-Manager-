# Password-Generator-and-Manager-
Generate and manage password on the go.

In this code, we create a PasswordManager class that inherits from QMainWindow and implements the GUI for our password manager. We create the widgets using the PyQt5 classes, connect the buttons to their respective functions, and set up the layout using QFormLayout.

When the user clicks on the "Generate Password" button, the generate_password function is called, which generates a random password of length 12 and displays it in the password field using self.password_entry.setText. When the user clicks on the "Save" button, the save_password function is called, which saves the website, email, and password information to a text file named passwords.txt.

We also use the pyperclip library to copy the generated password to the clipboard using pyperclip.copy(password). Finally, we use QMessageBox to display a message box when the password is saved successfully.
