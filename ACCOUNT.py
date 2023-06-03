from Data import data



class Manage_User:
    def __init__(self, usernaame, firstname, lastname, email):
        self.username = usernaame
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def login(self, password):
