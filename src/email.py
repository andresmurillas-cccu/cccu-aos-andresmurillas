import exchangelib

class Emails:
    
    email = ""
    username = ""
    password = ""
    
    
    def __init__(self):
        pass
    
    def setup(self):
        self.email = input("email: ")
        self.username = input("user name: ")
        self.password = input("password: ")

    def 