import tkinter as tk
import password_manager


def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website and username and password:
        password_manager.add_password(website, username, password)
        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Manager")
root.geometry("500x350")

root.configure(bg="#f0f0f0")
root.iconbitmap("icon.ico")

website_label = tk.Label(root, text="Website:", font=("Arial", 14), bg="#f0f0f0")
website_label.pack(pady=5)

website_entry = tk.Entry(root, font=("Arial", 12))
website_entry.pack(pady=5)

username_label = tk.Label(root, text="Username:", font=("Arial", 14), bg="#f0f0f0")
username_label.pack(pady=5)

username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:", font=("Arial", 14), bg="#f0f0f0")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Password", font=("Arial", 12), command=add_password)
add_button.pack(pady=10)

show_button = tk.Button(root, text="Show Passwords", font=("Arial", 12), command=password_manager.show_passwords)
show_button.pack(pady=5)

root.mainloop()
