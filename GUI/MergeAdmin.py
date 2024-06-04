import tkinter as tk
from tkinter import messagebox
import os
import Helper.Status as con

def save_to_file(institution_data):
    try:
        desktop_path = os.path.join(os.path.expanduser('~'),'Desktop')
        file_name = 'notepad_file.txt'
        file_path = os.path.join(desktop_path,file_name)
        
        with open(file_path, 'w') as file:
            file.write(str(institution_data))
        
        messagebox.showinfo("Success", f"Data has been written to {file_path}")

        if con.is_internet_available():
            if con.is_testnet_connected():
                print("Hello World")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


save_to_file("Kite")
