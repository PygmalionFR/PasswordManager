# Password Manager

This project is a simple password manager created using Python and the Tkinter library for the graphical user interface. It stores website, username, and password information in a SQLite database. You can add, view, edit, and delete password entries using this application.

## Prerequisites

- Python 3.x should be installed on your system.
- Make sure you have the Tkinter library, which is typically included in standard Python installations.

## How to Run the Application

1. Download or clone the source code to your local directory.
2. Ensure that the `icon.ico` file is present in the same directory as the Python script.
3. Run the application by executing the `password_manager.py` Python file.

## Features

### Add a Password

1. Open the Password Manager application.
2. Enter the website, username, and password in the appropriate fields.
3. Click the "Add Password" button to save the information to the database.

### Show Passwords

1. Click the "Show Passwords" button to display all saved passwords in the database.
2. A window will open with a list of websites, usernames, and passwords.

### Edit a Password

1. In the window displaying the passwords, click the "Edit" button corresponding to the entry you want to modify.
2. A new window will open, allowing you to edit the website, username, and password information.
3. Click the "Save Changes" button to save the changes.

### Delete a Password

1. In the window displaying the passwords, click the "Delete" button corresponding to the entry you want to delete.
2. A confirmation dialog will appear to confirm the deletion.
3. Click "Yes" to delete the password from the database.

## Notes

- Passwords are stored locally in a SQLite database named `passwords.db`.
- Make sure to securely back up your passwords as they are not recoverable in case of database loss.
