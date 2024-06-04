from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox
import os
import re
from datetime import datetime

def validate_alpha_space(char):
    return all(x.isalpha() or x.isspace() for x in char)

def validate_alpha(char):
    return char.isalpha() or char == ""

def validate_digit(char, max_len):
    return (char.isdigit() and len(char) <= max_len) or char == ""

def validate_digit_8_or_10(char):
    return char.isdigit() and len(char) <= 10 or char == ""

def validate_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Selected file does not exist.")
            return
        file_entry.config(state=NORMAL)
        file_entry.delete(0, END)
        file_entry.insert(0, file_path)
        file_entry.config(state="readonly")
        folder_entry.config(state=NORMAL)
        folder_entry.delete(0, END)
        folder_entry.config(state="readonly")

def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        if not os.path.exists(folder_path):
            messagebox.showerror("Error", "Selected folder does not exist.")
            return
        folder_entry.config(state=NORMAL)
        folder_entry.delete(0, END)
        folder_entry.insert(0, folder_path)
        folder_entry.config(state="readonly")
        file_entry.config(state=NORMAL)
        file_entry.delete(0, END)
        file_entry.config(state="readonly")

def submit():
    try:
        # Validate fields
        first_name = e1.get().strip()
        middle_name = e2.get().strip()
        last_name = e3.get().strip()
        gender = gender_combobox.get().strip()
        day = e4_dd.get().strip()
        month = e4_mm.get().strip()
        year = e4_yyyy.get().strip()
        student_contact = e4_1.get().strip()
        student_email = e4_2.get().strip()
        aadhar = e5.get().strip()
        institution_name = e6.get().strip()
        accreditation_status = e7.get().strip()
        email1 = e8_1.get().strip()
        email2 = e8_2.get().strip()
        contact_no1 = e9_1.get().strip()
        telephone_no1 = e9_2.get().strip()
        address = e10.get().strip()
        date_of_issuance = e11.get().strip()
        type_of_credential = e12.get().strip()
        file_path = file_entry.get().strip()
        folder_path = folder_entry.get().strip()

        if not first_name.isalpha():
            raise ValueError("First Name must contain only letters.")
        
        if not middle_name.isalpha():
            raise ValueError("Middle Name must contain only letters.")
        
        if not last_name.isalpha():
            raise ValueError("Last Name must contain only letters.")

        if gender not in ["Male", "Female", "Other"]:
            raise ValueError("Gender must be one of Male, Female, or Other.")
        
        if not day.isdigit() or not (1 <= int(day) <= 31):
            raise ValueError("Day must be a number between 1 and 31.")
        
        if not month.isdigit() or not (1 <= int(month) <= 12):
            raise ValueError("Month must be a number between 1 and 12.")
        
        if not year.isdigit() or not (1980 <= int(year) <= datetime.now().year):
            raise ValueError(f"Year must be a number between 1980 and {datetime.now().year}.")
        
        if not student_contact.isdigit() or len(student_contact) not in {8, 10}:
            raise ValueError("Student Contact Number must be either 8 or 10 digits.")
        
        if not student_email or not validate_email(student_email):
            raise ValueError("Invalid Student Email format.")
        
        if not aadhar.isdigit() or len(aadhar) != 12:
            raise ValueError("Aadhar Number must be a 12-digit number.")
        
        if not institution_name or not validate_alpha_space(institution_name):
            raise ValueError("Institution Name must contain only letters and spaces.")
        
        if not accreditation_status:
            raise ValueError("Institution Accreditation Status cannot be empty.")
        
        if not email1 or not validate_email(email1):
            raise ValueError("Invalid Email 1 format.")
        
        if not email2 or not validate_email(email2):
            raise ValueError("Invalid Email 2 format.")
        
        if not contact_no1.isdigit() or len(contact_no1) not in {8, 10}:
            raise ValueError("Contact Number must be either 8 or 10 digits.")
        
        if not telephone_no1.isdigit() or len(telephone_no1) not in {8, 10}:
            raise ValueError("Telephone Number must be either 8 or 10 digits.")
        
        if not address:
            raise ValueError("Address cannot be empty.")
        
        if not date_of_issuance:
            raise ValueError("Date of Issuance cannot be empty.")

        if not type_of_credential:
            raise ValueError("Type of Credential cannot be empty.")
        
        if not file_path and not folder_path:
            raise ValueError("You must choose either a file or a folder.")
        
        if file_path and folder_path:
            raise ValueError("You cannot choose both a file and a folder. Please select only one.")

        # Collect data
        student_data = {
            "First Name": first_name.lower(),
            "Middle Name": middle_name.lower(),
            "Last Name": last_name.lower(),
            "Gender": gender,
            "Date of Birth": f"{day.zfill(2)}-{month.zfill(2)}-{year}",
            "Student Contact": student_contact,
            "Student Email": student_email.lower(),
            "Aadhar Number": aadhar,
            "Institution Name": institution_name,
            "Institution Accreditation Status": accreditation_status,
            "Institution Email 1": email1.lower(),
            "Institution Email 2": email2.lower(),
            "Institution Contact No.": contact_no1,
            "Institution Telephone No.": telephone_no1,
            "Institution Address": address,
            "Date of Issuance": date_of_issuance,
            "Type of Credential": type_of_credential.lower(),
            "File Path": file_path,
            "Folder Path": folder_path
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
    gender_combobox.set("")
    e4_dd.delete(0, END)
    e4_mm.delete(0, END)
    e4_yyyy.delete(0, END)
    e4_1.delete(0, END)
    e4_2.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8_1.delete(0, END)
    e8_2.delete(0, END)
    e9_1.delete(0, END)
    e9_2.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e11.insert(0, datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    e12.delete(0, END)
    file_entry.config(state=NORMAL)
    file_entry.delete(0, END)
    file_entry.config(state="readonly")
    folder_entry.config(state=NORMAL)
    folder_entry.delete(0, END)
    folder_entry.config(state="readonly")

parent = Tk()
parent.title("Student Data Entry")
parent.geometry("600x900")
parent.configure(bg="#f7f7f7")

style = ttk.Style(parent)
style.configure("TLabel", font=("Helvetica", 12), foreground="#000000", background="#f7f7f7")
style.configure("TButton", font=("Helvetica", 12), background="#007acc", foreground="#000000")
style.map("TButton", background=[('active', '#005fa3')])

vcmd_alpha = (parent.register(validate_alpha), '%P')
vcmd_alpha_space = (parent.register(validate_alpha_space), '%P')
vcmd_digit_2 = (parent.register(lambda P: validate_digit(P, 2)), '%P')
vcmd_digit_4 = (parent.register(lambda P: validate_digit(P, 4)), '%P')
vcmd_digit_12 = (parent.register(lambda P: validate_digit(P, 12)), '%P')
vcmd_digit_8_or_10 = (parent.register(validate_digit_8_or_10), '%P')

label_frame_1 = Frame(parent, bg="#f7f7f7")
label_frame_1.grid(row=0, column=0, padx=10, pady=10, sticky=E)
label_frame_2 = Frame(parent, bg="#f7f7f7")
label_frame_2.grid(row=0, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_1, text="Student First Name").grid(row=0, column=0, padx=10, pady=10, sticky=E)
e1 = ttk.Entry(label_frame_1, font=("Helvetica", 12), validate="key", validatecommand=vcmd_alpha)
e1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_1, text="Student Middle Name").grid(row=1, column=0, padx=10, pady=10, sticky=E)
e2 = ttk.Entry(label_frame_1, font=("Helvetica", 12), validate="key", validatecommand=vcmd_alpha)
e2.grid(row=1, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_1, text="Student Last Name").grid(row=2, column=0, padx=10, pady=10, sticky=E)
e3 = ttk.Entry(label_frame_1, font=("Helvetica", 12), validate="key", validatecommand=vcmd_alpha)
e3.grid(row=2, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_1, text="Student Gender").grid(row=3, column=0, padx=10, pady=10, sticky=E)
gender_combobox = ttk.Combobox(label_frame_1, font=("Helvetica", 12), values=["Male", "Female", "Other"])
gender_combobox.grid(row=3, column=1, padx=10, pady=10, sticky=W)
gender_combobox.set("")

ttk.Label(label_frame_1, text="Student DOB (dd-mm-yyyy)").grid(row=4, column=0, padx=10, pady=10, sticky=E)
dob_frame = Frame(label_frame_1, bg="#f0f4f7")
dob_frame.grid(row=4, column=1, padx=10, pady=10, sticky=W)
e4_dd = ttk.Entry(dob_frame, width=3, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_2)
e4_dd.grid(row=0, column=0)
ttk.Label(dob_frame, text="-", background="#f0f4f7").grid(row=0, column=1)
e4_mm = ttk.Entry(dob_frame, width=3, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_2)
e4_mm.grid(row=0, column=2)
ttk.Label(dob_frame, text="-", background="#f0f4f7").grid(row=0, column=3)
e4_yyyy = ttk.Entry(dob_frame, width=5, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_4)
e4_yyyy.grid(row=0, column=4)

ttk.Label(label_frame_1, text="Student Contact").grid(row=5, column=0, padx=10, pady=10, sticky=E)
e4_1 = ttk.Entry(label_frame_1, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_8_or_10)
e4_1.grid(row=5, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_1, text="Student Email").grid(row=6, column=0, padx=10, pady=10, sticky=E)
e4_2 = ttk.Entry(label_frame_1, font=("Helvetica", 12))
e4_2.grid(row=6, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_1, text="Student Aadhar Number").grid(row=7, column=0, padx=10, pady=10, sticky=E)
e5 = ttk.Entry(label_frame_1, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_12)
e5.grid(row=7, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_1, text="Institution Name").grid(row=8, column=0, padx=10, pady=10, sticky=E)
e6 = ttk.Entry(label_frame_1, font=("Helvetica", 12))
e6.grid(row=8, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_1, text="Institution Accreditation Status").grid(row=9, column=0, padx=10, pady=10, sticky=E)
e7 = ttk.Entry(label_frame_1, font=("Helvetica", 12))
e7.grid(row=9, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_2, text="Institution Email 1").grid(row=10, column=0, padx=10, pady=10, sticky=E)
e8_1 = ttk.Entry(label_frame_2, font=("Helvetica", 12))
e8_1.grid(row=10, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_2, text="Institution Email 2").grid(row=11, column=0, padx=10, pady=10, sticky=E)
e8_2 = ttk.Entry(label_frame_2, font=("Helvetica", 12))
e8_2.grid(row=11, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_2, text="Institution Contact No.").grid(row=12, column=0, padx=10, pady=10, sticky=E)
e9_1 = ttk.Entry(label_frame_2, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_8_or_10)
e9_1.grid(row=12, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_2, text="Institution Contact No.").grid(row=13, column=0, padx=10, pady=10, sticky=E)
e9_2 = ttk.Entry(label_frame_2, font=("Helvetica", 12), validate="key", validatecommand=vcmd_digit_8_or_10)
e9_2.grid(row=13, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_2, text="Institution Address").grid(row=14, column=0, padx=10, pady=10, sticky=E)
e10 = ttk.Entry(label_frame_2, font=("Helvetica", 12))
e10.grid(row=14, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_2, text="Credential Issued On (dd-mm-yyyy hh:mm:ss)").grid(row=15, column=0, padx=10, pady=10, sticky=E)
e11 = ttk.Entry(label_frame_2, font=("Helvetica", 12))
e11.grid(row=15, column=1, padx=10, pady=10, sticky=W)
e11.insert(0, datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

ttk.Label(label_frame_2, text="Credential Type").grid(row=16, column=0, padx=10, pady=10, sticky=E)
e12 = ttk.Entry(label_frame_2, font=("Helvetica", 12))
e12.grid(row=16, column=1, padx=10, pady=10, sticky=W)

ttk.Label(label_frame_2, text="Choose File").grid(row=17, column=0, padx=10, pady=10, sticky=E)
file_frame = Frame(label_frame_2, bg="#f0f4f7")
file_frame.grid(row=17, column=1, padx=10, pady=10, sticky=W)
file_button = ttk.Button(file_frame, text="Choose File", command=choose_file)
file_button.grid(row=0, column=0, padx=5)
file_entry = ttk.Entry(file_frame, font=("Helvetica", 12), state="readonly")
file_entry.grid(row=0, column=1, padx=5)

ttk.Label(label_frame_2, text="Choose Folder").grid(row=18, column=0, padx=10, pady=10, sticky=E)
folder_frame = Frame(label_frame_2, bg="#f0f4f7")
folder_frame.grid(row=18, column=1, padx=10, pady=10, sticky=W)
folder_button = ttk.Button(folder_frame, text="Choose Folder", command=choose_folder)
folder_button.grid(row=0, column=0, padx=5)
folder_entry = ttk.Entry(folder_frame, font=("Helvetica", 12), state="readonly")
folder_entry.grid(row=0, column=1, padx=5)

submit_button = ttk.Button(parent, text="Submit", command=submit)
submit_button.grid(row=19, column=0, columnspan=2, pady=20)

parent.mainloop()
