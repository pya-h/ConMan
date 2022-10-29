from tkinter import simpledialog, messagebox
import tkinter as tk
from contact import *
from edit_contact import EditContactUI
from filter import FilterUI

class ContactsUI:

    def __init__(self) -> None:
        self.app = None
        self.edit_form = None

    def ask(self, title, question):
        inputbox = tk.Tk()
        inputbox.withdraw()
        return simpledialog.askstring(title, question, parent=inputbox)

    def start(self):
        self.app = tk.Tk()
        self.app.configure(bg='lightgray')
        self.app.title("Contact Manager")
        self.lst_contacts = tk.Listbox(self.app, width=100, height=40)
        self.lst_contacts.grid(row=0, column=0, columnspan=2, rowspan=100, sticky='nwse', padx=(10, 10), pady=(5, 20))
        self.lst_contacts.bind("<<ListboxSelect>>", self.select_contact)

        self.listbox_scrollbar = tk.Scrollbar(self.app)
        self.lst_contacts.config(yscrollcommand=self.listbox_scrollbar.set)
        self.listbox_scrollbar.config(command=self.lst_contacts.yview)


        self.btn_filter = tk.Button(self.app, text="Filter", command=self.filter, height=2)
        self.btn_filter.grid(row=95, column=2,  padx=(10,10), pady=(5,20))
        self.btn_filter.config(font=("Calibari", 12), width=10)
        
        self.btn_edit = tk.Button(self.app, text="Edit", command=self.edit, height=2)
        self.btn_edit.grid(row=96, column=2,  padx=(10,10), pady=(5,20))
        self.btn_edit.config(font=("Calibari", 12), width=10)
        
        self.btn_add = tk.Button(self.app, text="Add", command=self.add, height=2)
        self.btn_add.grid(row=97, column=2,  padx=(10,10), pady=(5,20))
        self.btn_add.config(font=("Calibari", 12), width=10)
                
        self.btn_remove = tk.Button(self.app, text="Remove", command=self.remove, height=2)
        self.btn_remove.grid(row=98, column=2,  padx=(10,10), pady=(5,20))
        self.btn_remove.config(font=("Calibari", 12), width=10)
        
        self.btn_exit = tk.Button(self.app, text="Exit", command=self.close, height=2)
        self.btn_exit.grid(row=99, column=2,  padx=(10,10), pady=(5,20))
        self.btn_exit.config(font=("Calibari", 12), width=10)

        self.app.minsize(800,600)
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.mainloop()

    def add(self):
        fn = self.ask("First Name", "What\'s your first name?")
        ln = self.ask("Last Name", "What\'s your last name?")
        age = self.ask("Age", "How old are you?")
        phone = self.ask("Phone Number", "What\'s your phone number?")
        Contact(fn, ln, age, phone)
        # self.lst_contacts.insert(tk.END, Contact.All[-1])
        self.update()
        Contact.Count()
        
    def update(self):
        self.lst_contacts.delete(0, tk.END)
        for contact in Contact.All:
            self.lst_contacts.insert(tk.END, contact)
        
    def select_contact(self, event):
        selection = event.widget.curselection()
        Contact.SelectedIndex = selection[0]

    def remove(self):
        if Contact.SelectedIndex >= 0 and Contact.SelectedIndex < len(Contact.All):
            if messagebox.askquestion("R U Sure?", f"Are tou sure you want to remove `{Contact.All[Contact.SelectedIndex].fullname()}`?") == messagebox.YES:
                del Contact.All[Contact.SelectedIndex]
                self.update()
        else:
            messagebox.showerror("No Contact Selected", "In order to remove a contact, you must first select one!")

    def edit(self):
        # if (self.edit_form is None or self.edit_form.app is None) and Contact.SelectedIndex >= 0 and Contact.SelectedIndex < len(Contact.All):
        if self.edit_form is None or self.edit_form.app is None:
            if Contact.SelectedIndex >= 0 and Contact.SelectedIndex < len(Contact.All):
                self.edit_form = EditContactUI(self.update)
                self.edit_form.start()
            else:
                messagebox.showerror("No Item Selected", "For editting, you need to first select a contact!")
        else:
            messagebox.showerror("Edit OnProgress", "First finish your previous edit then go for a new edit!")

    def filter(self):
        FilterUI().start()

    def close(self):
        # ON CLOSE EVENT
        if self.edit_form and self.edit_form.app:
            try:
                self.edit_form.app.destroy()
            except:
                self.edit_form = None
        self.app.destroy()

if __name__ == '__main__':
    ContactsUI().start()
        