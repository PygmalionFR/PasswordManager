import tkinter as tk
from tkinter import messagebox
import sqlite3


def show_passwords():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT website, username, password FROM passwords")
    passwords = c.fetchall()
    conn.close()

    if not passwords:
        messagebox.showinfo("No Passwords", "No passwords found in the database.")
        return

    password_window = tk.Toplevel()
    password_window.title("Password Manager - Passwords")
    password_window.geometry("700x400")
    password_window.iconbitmap("icon.ico")

    password_window.configure(bg="#f0f0f0")

    # Étiquettes pour les titres des colonnes
    tk.Label(password_window, text="Website", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(password_window, text="Username", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=0, column=1, padx=10, pady=5)
    tk.Label(password_window, text="Password", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=0, column=2, padx=10, pady=5)
    tk.Label(password_window, font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=0, column=3, padx=10, pady=5)

    for i, password_data in enumerate(passwords, start=1):
        website, username, password = password_data

        tk.Label(password_window, text=website, font=("Arial", 12), bg="#f0f0f0").grid(row=i, column=0, padx=10, pady=5)
        tk.Label(password_window, text=username, font=("Arial", 12), bg="#f0f0f0").grid(row=i, column=1, padx=10,
                                                                                        pady=5)
        tk.Label(password_window, text=password, font=("Arial", 12), bg="#f0f0f0").grid(row=i, column=2, padx=10,
                                                                                        pady=5)

        tk.Button(password_window, text="Delete", font=("Arial", 12), bg="red",
                  command=lambda p=password_data: delete_password(p, password_window)).grid(row=i, column=3, padx=5, pady=5)
        tk.Button(password_window, text="Edit", font=("Arial", 12), bg="green",
                  command=lambda p=password_data: edit_password(p)).grid(row=i, column=4, padx=5, pady=5)

def delete_password(password, password_window):
    website, username, password = password

    confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the password for {website}?")
    if confirm:
        conn = sqlite3.connect("passwords.db")
        c = conn.cursor()
        c.execute("DELETE FROM passwords WHERE website=?", (website,))
        conn.commit()
        conn.close()

        password_window.destroy()
        show_passwords()

def edit_password(password):
    website, username, password = password

    edit_window = tk.Toplevel()
    edit_window.title("Edit Password")
    edit_window.geometry("300x200")
    edit_window.iconbitmap("icon.ico")

    edit_window.configure(bg="#f0f0f0")

    tk.Label(edit_window, text="Website:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    website_entry = tk.Entry(edit_window, font=("Arial", 12))
    website_entry.pack(pady=5)
    website_entry.insert(0, website)

    tk.Label(edit_window, text="Username:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    username_entry = tk.Entry(edit_window, font=("Arial", 12))
    username_entry.pack(pady=5)
    username_entry.insert(0, username)

    tk.Label(edit_window, text="Password:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    password_entry = tk.Entry(edit_window, show="*", font=("Arial", 12))
    password_entry.pack(pady=5)
    password_entry.insert(0, password)

    def save_changes():
        new_website = website_entry.get()
        new_username = username_entry.get()
        new_password = password_entry.get()

        conn = sqlite3.connect("passwords.db")
        c = conn.cursor()
        c.execute("UPDATE passwords SET website=?, username=?, password=? WHERE website=?", (new_website, new_username, new_password, website))
        conn.commit()
        conn.close()

        edit_window.destroy()
        show_passwords()

    save_button = tk.Button(edit_window, text="Save Changes", font=("Arial", 12), bg="green", command=save_changes)
    save_button.pack(pady=10)
