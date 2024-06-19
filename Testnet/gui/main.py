import tkinter as tk
import re
import  json
import api.ReadFileData
import subprocess
import api.smartcontract.helper.FirebaseHelper as fire
from tkinter import messagebox
from CredVerify import CredVerify
from AddAdminGUI import AddAdminGUI
import AddStudentGUI

def admin_login(username, password):
    byte_data = api.ReadFileData.read_ipfs_content("QmSygUpFJLpzDPxYdjxy57u7wLm3hgHpDgYAsxmSFV9Brj")
    json_str = byte_data.decode('utf-8')
    data = json.loads(json_str)
    search_term = username
    search_term1 = password
    filtered_results = [entry for entry in data if 
                        (search_term == entry.get('Institution Name', '') or
                         search_term == entry.get('Email 1', '') or
                         search_term == entry.get('Email 2', '') or
                         search_term == entry.get('Contact 1', '') or
                         search_term == entry.get('Contact 2', ''))
                        and (search_term1 == entry.get('UID', ''))]
    
    if filtered_results:
        for result in filtered_results:
            messagebox.showinfo("Success", "Admin logged in successfully!")
            AddStudentGUI.main()
    else:
        messagebox.showerror("Error", "No matching data found for the provided credentials.")

def developer_login(username, password):
    if fire.authenticate_developer(username, password):
        messagebox.showinfo("Success", "Developer logged in successfully!")
        dev = AddAdminGUI()
    else:
        messagebox.showerror("Error", "Invalid Credentials!!")

def show_login_fields(role):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text=f"{role} Login", font=("Arial", 20, "bold"), fg="black", bg="#50c878").pack(pady=15)
    tk.Label(frame, text="Username / Email ID / Phone No.", font=("Arial", 15, "bold"), fg="black", bg="#50c878").pack(pady=10)
    entry_username = tk.Entry(frame, font=("Arial", 15))
    entry_username.pack(pady=10)

    tk.Label(frame, text="Password", font=("Arial", 15, "bold"), fg="black", bg="#50c878").pack(pady=10)
    entry_password = tk.Entry(frame, show="*", font=("Arial", 15))
    entry_password.pack(pady=10)

    def on_login():
        username = entry_username.get()
        password = entry_password.get()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if role == "Admin":
            admin_login(username, password)
        elif role == "Developer":
            developer_login(username, password)
        else:
            messagebox.showerror("Error", f"Unknown role '{role}'")

    tk.Button(frame, text="Login", command=on_login, font=("Arial", 12, "bold"), fg="white", bg="#61afef", activebackground="#3b4048").pack(pady=20)

def handle_student_click():
    stu = CredVerify()

root = tk.Tk()
root.title("Login UI")
root.geometry("400x400")
root.configure(bg="#282c34")

frame = tk.Frame(root, bg="#50c878")
frame.pack(expand=True, fill="both")

button_style = {"font": ("Arial", 14, "bold"),"fg": "white","bg": "#61afef","activebackground": "#50c878","width": 15,"pady": 10}

tk.Label(root, text="Welcome to the Login Portal", font=("Arial", 18, "bold"), fg="white", bg="#282c34").pack(pady=20)

tk.Button(root, text="Developer", command=lambda: show_login_fields("Developer"), **button_style).pack(pady=10)
tk.Button(root, text="Admin", command=lambda: show_login_fields("Admin"), **button_style).pack(pady=10)
tk.Button(root, text="Student", command=handle_student_click, **button_style).pack(pady=10)

root.mainloop()
