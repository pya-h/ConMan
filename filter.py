from tkinter import messagebox
import tkinter as tk
from contact import *

class FilterUI:

    def __init__(self) -> None:
        self.app = None

    def start(self):
        self.app = tk.Tk()
        self.app.configure(bg='lightgray')
        self.app.title("Filter Contacts")
        self.lst_contacts = tk.Listbox(self.app, width=150, height=40)
        self.lst_contacts.grid(row=0, column=0, columnspan=2, rowspan=100, sticky='nwse', padx=(10, 10), pady=(5, 20))
        # self.lst_contacts.bind("<<ListboxSelect>>", self.select_contact)

        self.listbox_scrollbar = tk.Scrollbar(self.app)
        self.lst_contacts.config(yscrollcommand=self.listbox_scrollbar.set)
        self.listbox_scrollbar.config(command=self.lst_contacts.yview)


        self.lbl_sub_name = tk.Label(self.app, text="Part of name:")
        self.lbl_sub_name.grid(row=93, column=2, columnspan=2, padx=(10,10), pady=(5,1))
        self.lbl_sub_name.config(font=("Calibari", 12), width=30, bg="lightgray")
        self.txt_sub_name = tk.Entry(self.app)
        self.txt_sub_name.grid(row=94, column=2, columnspan=2, padx=(10,10), pady=(5,20))
        self.txt_sub_name.config(font=("Calibari", 12), width=50)

        self.lbl_min_age = tk.Label(self.app, text="Min Age:")
        self.lbl_min_age.grid(row=95, column=2, columnspan=1, padx=(10,10), pady=(5,1))
        self.lbl_min_age.config(font=("Calibari", 12), width=30, bg="lightgray")
        self.txt_min_age = tk.Entry(self.app,)
        self.txt_min_age.grid(row=96, column=2, padx=(10,10), pady=(5,20))
        self.txt_min_age.config(font=("Calibari", 12), width=25)
        self.lbl_max_age = tk.Label(self.app, text="Max Age:")
        self.lbl_max_age.grid(row=95, column=3, columnspan=1, padx=(10,10), pady=(5,1))
        self.lbl_max_age.config(font=("Calibari", 12), width=30, bg="lightgray")
        self.txt_max_age = tk.Entry(self.app,)
        self.txt_max_age.grid(row=96, column=3, padx=(10,30),pady=(5,20))
        self.txt_max_age.config(font=("Calibari", 12), width=25)

        self.lbl_sub_phone = tk.Label(self.app, text="Part of Phone number:")
        self.lbl_sub_phone.grid(row=97, column=2, columnspan=2, padx=(10,10), pady=(5,1))
        self.lbl_sub_phone.config(font=("Calibari", 12), width=30, bg="lightgray")      
        self.txt_sub_phone = tk.Entry(self.app)
        self.txt_sub_phone.grid(row=98, column=2,  columnspan=2, padx=(10,10), pady=(5,20))
        self.txt_sub_phone.config(font=("Calibari", 12), width=50)

        self.btn_search = tk.Button(self.app, text="Exit", command=self.close, height=2)
        self.btn_search.grid(row=99, column=2, columnspan=1, padx=(10,10), pady=(5,20))
        self.btn_search.config(font=("Calibari", 12), width=18)

        self.btn_search = tk.Button(self.app, text="Search", command=self.search, height=2)
        self.btn_search.grid(row=99, column=3, columnspan=1, padx=(10,10), pady=(5,20))
        self.btn_search.config(font=("Calibari", 12), width=18)

        self.app.minsize(800,600)
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.mainloop()

    def search(self):
        self.lst_contacts.delete(0, tk.END)
        for contact in Contact.All:
            if self.txt_sub_name.get() and not self.txt_sub_name.get() in contact.fullname() or \
                self.txt_sub_phone.get() and not self.txt_sub_phone.get() in contact.phone or \
                self.txt_min_age.get() and float(self.txt_min_age.get()) > float(contact.age) or \
                self.txt_max_age.get() and float(self.txt_max_age.get()) < float(contact.age):
                    continue
            self.lst_contacts.insert(tk.END, contact)

    def close(self):
        self.app.destroy()

if __name__ == '__main__':
    FilterUI().start()
        
