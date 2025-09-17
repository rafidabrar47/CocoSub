import tkinter as tk
from tkinter import messagebox

# Dictionary to store users
users = {}

# Function to handle login
def login():
    user = username_entry.get()
    pwd = password_entry.get()
    
    if user in users and users[user] == pwd:
        messagebox.showinfo("Login Success", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to handle registration
def register():
    user = reg_username_entry.get()
    pwd = reg_password_entry.get()
    
    if user in users:
        messagebox.showerror("Registration Failed", "Username already exists!")
    elif user == "" or pwd == "":
        messagebox.showerror("Registration Failed", "Username and password cannot be empty")
    else:
        users[user] = pwd
        messagebox.showinfo("Registration Success", f"User {user} registered successfully!")
        reg_username_entry.delete(0, tk.END)
        reg_password_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Login and Registration Page")
root.geometry("400x300")

# --- Login Section ---
tk.Label(root, text="Login", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()
tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
tk.Button(root, text="Login", command=login).pack(pady=10)

# Separator
tk.Label(root, text="---------------- OR ----------------").pack(pady=10)

# --- Registration Section ---
tk.Label(root, text="Register", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Username").pack()
reg_username_entry = tk.Entry(root)
reg_username_entry.pack()
tk.Label(root, text="Password").pack()
reg_password_entry = tk.Entry(root, show="*")
reg_password_entry.pack()
tk.Button(root, text="Register", command=register).pack(pady=10)

root.mainloop()

