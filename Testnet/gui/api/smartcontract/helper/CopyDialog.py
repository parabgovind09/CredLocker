import tkinter as tk
from tkinter import messagebox, simpledialog

class CopyableDialog(simpledialog.Dialog):
    def __init__(self, parent, title, text, subtext, msg_title, msg):
        self.text = text
        self.subtext = subtext
        self.msg_title = msg_title
        self.msg = msg
        super().__init__(parent, title)

    def body(self, parent):
        tk.Label(parent, text=self.subtext).pack(padx=10, pady=10)
        self.entry = tk.Entry(parent, width=50)
        self.entry.insert(0, self.text)
        self.entry.config(state='readonly')
        self.entry.pack(padx=10, pady=10)
        return self.entry

    def buttonbox(self):
        box = tk.Frame(self)

        w = tk.Button(box, text="Copy", width=10, command=self.copy_to_clipboard)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="OK", width=10, command=self.ok)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.text)
        self.update()
        messagebox.showinfo(self.msg_title,self.msg)
