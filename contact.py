
class Contact:
    NumberOfObjects = 0
    All = []
    SelectedIndex = -1
    def __init__(self, fn, ln, age, phone) -> None:
        self.fn = fn
        self.ln = ln
        self.age = age
        self.phone = phone
        Contact.NumberOfObjects += 1
        Contact.All.append(self)

    @staticmethod
    def Count():
        print("Number of all defined contacts: ", Contact.NumberOfObjects)


    def fullname(self):
        return f'{self.fn} {self.ln}'
        
    def __str__(self) -> str:
        return f'{self.fn} {self.ln}                         {self.age}                         {self.phone}'