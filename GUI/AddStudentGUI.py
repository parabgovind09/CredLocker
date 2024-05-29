from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def validate_alpha(char):
    return char.isalpha() or char == ""

def validate_digit(char, max_len):
    return char.isdigit() and len(char) <= max_len or char == ""

def submit():
    try:
        # Validate fields
        first_name = e1.get().strip()
        middle_name = e2.get().strip()
        last_name = e3.get().strip()
        day = e4_dd.get().strip()
        month = e4_mm.get().strip()
        year = e4_yyyy.get().strip()
        aadhar = e5.get().strip()

        if not first_name.isalpha():
            raise ValueError("First Name must contain only letters.")
        
        if not middle_name.isalpha():
            raise ValueError("Middle Name must contain only letters.")
        
        if not last_name.isalpha():
            raise ValueError("Last Name must contain only letters.")
        
        if not day.isdigit() or not (1 <= int(day) <= 31):
            raise ValueError("Day must be a number between 1 and 31.")
        
        if not month.isdigit() or not (1 <= int(month) <= 12):
            raise ValueError("Month must be a number between 1 and 12.")
        
        if not year.isdigit() or not (1980 <= int(year) <= datetime.now().year):
            raise ValueError(f"Year must be a number between 1980 and {datetime.now().year}.")
        
        if not aadhar.isdigit() or len(aadhar) != 12:
            raise ValueError("Aadhar Number must be a 12-digit number.")

        # Collect data
        student_data = {
            "First Name": first_name,
            "Middle Name": middle_name,
            "Last Name": last_name,
            "Date of Birth": f"{day.zfill(2)}-{month.zfill(2)}-{year}",
            "Aadhar Number": aadhar
        }
        print(student_data)
        messagebox.showinfo("Success", "Student data submitted successfully!")
        clear_form()

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", "Please ensure all fields are filled out correctly.")

def clear_form():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4_dd.delete(0, END)
    e4_mm.delete(0, END)
    e4_yyyy.delete(0, END)
    e5.delete(0, END)

parent = Tk()
parent.title("Student Data Entry")
parent.geometry("500x500")
parent.configure(bg="#f7f7f7")

style = ttk.Style(parent)
style.configure("TLabel", font=("Helvetica", 12), foreground="#000000", background="#f7f7f7")
style.configure("TButton", font=("Helvetica", 12), background="#007acc", foreground="#000000")
style.map("TButton", background=[('active', '#005fa3')])

vcmd_alpha = (parent.register(validate_alpha), '%P')
vcmd_digit_2 = (parent.register(lambda P: validate_digit(P, 2)), '%P')
vcmd_digit_4 = (parent.register(lambda P: validate_digit(P, 4)), '%P')
vcmd_digit_12 = (parent.register(lambda P: validate_digit(P, 12)), '%P')

ttk.Label(parent, text="First Name").grid(row=0, column=0, padx=10, pady=10, sticky=E)
e1 = ttk.Entry(parent, font=("Helvetica", 12), validate="key", validatecommand=vcmd_alpha)
e1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

ttk.Label(parent, text="Middle Name").grid(row=1, column=0, padx=10, pady=10, sticky=E)
e2 = ttk.Entry(parent, font=("Helvetica", 12), validate="key", validatecommand=vcmd_alpha)
e2.grid(row=1, column=1, padx=10, pady=10, sticky=W)

ttk.Label(parent, text="Last Name").grid(row=2, column=0, padx=10, pady=10, sticky=E)
e3 = ttk.Entry(parent, font=("Helvetica", 12), validate="key", validatecommand=vcmd_alpha)
e3.grid(row=2, column=1, padx=10, pady=10, sticky=W)

ttk.Label(parent, text="Date of Birth (dd-mm-yyyy)").grid(row=3, column=0, padx=10, pady=10, sticky=E)
dob_frame = Frame(parent, bg="#f0f4f7")
dob_frame.grid(row=3, column=1, padx=10, pady=10, sticky=W)
e4_dd = ttk.Entry(dob_frame, width=3, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_2)
e4_dd.grid(row=0, column=0)
ttk.Label(dob_frame, text="-", background="#f0f4f7").grid(row=0, column=1)
e4_mm = ttk.Entry(dob_frame, width=3, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_2)
e4_mm.grid(row=0, column=2)
ttk.Label(dob_frame, text="-", background="#f0f4f7").grid(row=0, column=3)
e4_yyyy = ttk.Entry(dob_frame, width=5, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_4)
e4_yyyy.grid(row=0, column=4)

ttk.Label(parent, text="Aadhar Number").grid(row=4, column=0, padx=10, pady=10, sticky=E)
e5 = ttk.Entry(parent, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_12)
e5.grid(row=4, column=1, padx=10, pady=10, sticky=W)

submit_button = ttk.Button(parent, text="Submit", command=submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)

parent.mainloop()
