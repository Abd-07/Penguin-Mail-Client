import tkinter.messagebox as tkm

import login_file 
import database

from database import get_db_username_pass_peng_mail


mail_client_name = "Penguin Mail"
string_user_name = None

def check_user_data():
    global string_user_name

    string_user_name = login_file.entry_username_login.get()
    
    username,password = database.get_db_username_pass_peng_mail(login_file.entry_username_login.get())

    if str(login_file.entry_username_login.get()) == str(username) and str(login_file.entry_password.get()) == str(password) :
        tkm.showinfo("Message","You have Logged in ! \n Now close the Login window and Press on Compose in the Menu")
    else:
        tkm.showinfo("Message","Invalid Credentials.")