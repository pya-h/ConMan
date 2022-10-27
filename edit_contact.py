from pydoc import text
import tkinter as tk

from contact import Contact


class EditContactUI:

    def __init__(self, updater = None) -> None:
        self.app = None
        self.updater = updater

    def start(self):
        self.app = tk.Tk()
        self.app.title("Edit Contact")
        self.app.configure(bg="lightgray")
        self.app.minsize(800, 300)

        self.app.maxsize(900, 300)

        self.lbl_fn = tk.Label(self.app, text="First Name").grid(row = 0, column=0)
        self.txt_fn = tk.Entry(self.app, width=100)
        self.txt_fn.grid(row=0, column=1, columnspan=2, padx=(10,10), pady=(5,20)) 

        self.lbl_ln = tk.Label(self.app, text="Last Name").grid(row = 1, column=0)
        self.txt_ln = tk.Entry(self.app, width=100)
        self.txt_ln.grid(row=1, column=1, columnspan=2, padx=(10,10), pady=(5,20)) 

        self.lbl_age = tk.Label(self.app, text="Age").grid(row = 2, column=0)
        self.txt_age = tk.Entry(self.app, width=100)
        self.txt_age.grid(row=2, column=1, columnspan=2, padx=(10,10), pady=(5,20)) 

        self.lbl_phone = tk.Label(self.app, text="Phone Number").grid(row = 3, column=0)
        self.txt_phone = tk.Entry(self.app, width=100)
        self.txt_phone.grid(row=3, column=1, columnspan=2, padx=(10,10), pady=(5,20))
                
        self.btn_remove = tk.Button(self.app, text="Confirm", command=self.save, height=1)
        self.btn_remove.grid(row=4, column=2,  padx=(10,10), pady=(5,20))
        self.btn_remove.config(font=("Calibari", 12), width=25)
        
        self.btn_exit = tk.Button(self.app, text="Exit", command=self.close, height=1)
        self.btn_exit.grid(row=4, column=1,  padx=(10,10), pady=(5,20))
        self.btn_exit.config(font=("Calibari", 12), width=25)

        self.txt_fn.insert('0', Contact.All[Contact.SelectedIndex].fn)
        self.txt_ln.insert('0', Contact.All[Contact.SelectedIndex].ln)
        self.txt_age.insert('0', Contact.All[Contact.SelectedIndex].age)
        self.txt_phone.insert('0', Contact.All[Contact.SelectedIndex].phone)

        self.app.grid_columnconfigure(0, weight=1)
        self.app.mainloop()

    def close(self):
        self.app.destroy()
        self.app = None

    def save(self):
        Contact.All[Contact.SelectedIndex].fn = self.txt_fn.get()
        Contact.All[Contact.SelectedIndex].ln = self.txt_ln.get()
        Contact.All[Contact.SelectedIndex].age = self.txt_age.get()
        Contact.All[Contact.SelectedIndex].phone = self.txt_phone.get()
        if self.updater:
            self.updater()
            
        self.close()

if __name__ == '__main__':
    EditContactUI().start()