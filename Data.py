import sqlite3
import hashlib
from setting import *

class data:
    def __init__(self, database=Database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
    def exists(self, username):
        self.cursor.execute(f"""SELECT username from userdata where username='{username}'""")
        x = self.cursor.fetchall()
        if x:
            return True
        else:
            return False

    def Authenicate(self, username, password):
        self.cursor.execute(f"SELECT username, password from userdata where username='{username}' and password='{self.encrypt(password)}'")
        x = self.cursor.fetchall()
        if x:
            return True
        else:
            return False

    def encrypt(self, string:str):
        sha256= hashlib.sha256(string.encode("utf-8")).hexdigest()
        print(f"Given String [{string}] successfully encrypted.")
        return sha256



    def update(self, username:str, parameter:str, data:str):
        if self.Authenicate(username, input("password: ")):
            self.cursor.execute(f"update userdata set {parameter} = '{data}' where username = '{username}'")
            self.connection.commit()
            print(f"Updating [{parameter}] successfully done!")
        else:
            print(f"updating [{parameter}] failed. Invalid user access.")


    def delete(self, username, password):
        if self.exists(username):
            if self.Authenicate(username, password):
                self.cursor.execute(f"Delete  from userdata where username='{username}'")
                print(f"Record for [{username}] has been deleted permanently.")
                self.connection.commit()
            else:
                print("Invalid user access.")
        else:
            print(f"No record found.")


    def create_account(self, username, firstname, lastname, email,password):
        if self.exists(username):
            print(f"account with username [{username}] already exist.")
        else:
            self.cursor.execute("insert into userdata (username,firstname, lastname,email, password) values(?,?,?,?,?)", (username, firstname, lastname, email, self.encrypt(password)))
            self.connection.commit()
            print(f"Account with username [{username}] created successfully.")

    def create_table(self):
        self.cursor.execute(f"""CREATE TABLE {table}
                        (
                            id integer auto_increment primary key,
                            username varchar (250) NOT NULL,
                            firstname varchar(250) NOT NULL, 
                            lastname varchar (250), 
                            email varchar (250) NOT NULL,
                            password varchar (250) NOT NULL
                        )
                        """)

    def fetch_details(self, *args):
        if not args:
            self.cursor.execute(f""" SELECT * FROM {table}""")
        else:
            self.cursor.execute(f""" SELECT {args} from {table})""")
        result = self.cursor.fetchall()
        yield result

data_ = data("UserData.db")
data_.create_account("saurav2k01", "Saurav","Sharma", "saurav@fakemail.com","Saurav@23")
for i in data_.fetch_details():
    print(i)

