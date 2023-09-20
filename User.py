class User:
    def __init__(self,name, mail, age, phone_number):
        self.name = name
        self.mail = mail
        self.age = age
        self.phone_number = phone_number

    def change_name(self,new_name):
        self.name(new_name)

    def change_number(self,new_number):
        self.phone_number(new_number)

    def change_mail(self,new_mail):
        self.mail(new_mail)