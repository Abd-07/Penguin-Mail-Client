import tkinter.messagebox as tkm

import create_acc_file
import database

def write_user_info_into_database():
    tkm.showinfo("Message",f"Your Data was saved to the Data Base! \n Now close the 'create account' window and press 'Login to your Penguin Mail Account' on the Main Page \n Fill in the form and then press 'Login'")
    database.add_message(str(create_acc_file.entry_name.get()),str(create_acc_file.entry_surname.get()),str(create_acc_file.entry_username_create_acc.get()),str(create_acc_file.entry_password_penguin_mail.get()),str(create_acc_file.entry_email_address.get()),str(create_acc_file.entry_email_password.get()))