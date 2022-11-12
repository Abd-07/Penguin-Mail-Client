import tkinter as tk
from write_user_info_into_database_file import write_user_info_into_database

mail_client_name = "Penguin Mail"

entry_name_login = None
entry_name = None
entry_surname = None
entry_username_create_acc = None
entry_password_penguin_mail = None
entry_email_address = None
entry_email_password = None

def create_acc():
    global entry_name,entry_surname,entry_username_create_acc,entry_password_penguin_mail,entry_email_address,entry_email_password

    window_create_acc=tk.Tk()
    window_create_acc.title(f"{mail_client_name} - Account Creation Page")
    window_create_acc.geometry("355x480")
    window_create_acc.resizable(False,False)
    window_create_acc.configure(bg='#FF7514')

    #Text boxes
    entry_name = tk.Entry(window_create_acc,width=29,font=("Arial",13))
    entry_name.place(x=90,y=0)
    entry_surname = tk.Entry(window_create_acc,width=29,font=("Arial",13))
    entry_surname.place(x=90,y=50)
    entry_username_create_acc = tk.Entry(window_create_acc,width=29,font=("Arial",13))
    entry_username_create_acc.place(x=90,y=100)
    entry_password_penguin_mail = tk.Entry(window_create_acc,width=29,font=("Arial",13))
    entry_password_penguin_mail.place(x=90,y=150)

    entry_email_address = tk.Entry(window_create_acc,width=29,font=("Arial",13))
    entry_email_address.place(x=120,y=290)
    entry_email_password = tk.Entry(window_create_acc,width=29,font=("Arial",13))
    entry_email_password.place(x=120,y=340)

    #Buttons
    button_create_acc = tk.Button(window_create_acc,text=f'Create a {mail_client_name} Account',font=("Arial",16),fg='green')
    button_create_acc.place(x=55,y=405)
    button_create_acc["command"] = lambda selected_button = button_create_acc : write_user_info_into_database()
    
    #Label
    label_name=tk.Label(window_create_acc,text="Name",font=("Arial",16))
    label_name.place(x=0,y=0)
    label_surname=tk.Label(window_create_acc,text="Surname",font=("Arial",16))
    label_surname.place(x=0,y=50)
    label_username=tk.Label(window_create_acc,text="Username",font=("Arial",16))
    label_username.place(x=0,y=100)
    label_password=tk.Label(window_create_acc,text="Password",font=("Arial",16))
    label_password.place(x=0,y=150)

    label_email_info=tk.Label(window_create_acc,text="Sign In To Your Email :",font=("Arial",16))
    label_email_info.place(x=95,y=230)
    label_email_address=tk.Label(window_create_acc,text="Email Address",font=("Arial",15))
    label_email_address.place(x=0,y=290)
    label_email_password=tk.Label(window_create_acc,text="Email Password",font=("Arial",15))
    label_email_password.place(x=0,y=340)