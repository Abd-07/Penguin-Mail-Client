from importlib.metadata import entry_points
from pkgutil import get_data
from tkinter.font import BOLD
import yagmail
import tkinter as tk
import tkinter.messagebox as tkm
#from database import *

mail_client_name = "Penguin Mail"

window_welcome = tk.Tk()
window_welcome.title(f"{mail_client_name} - Main Page")
window_welcome.geometry("400x210")
window_welcome.resizable(False,False)
window_welcome.configure(bg='#E4A010')

entry_name = None

#Functions
def send_mail():
    from_ = 'email@gmail.com'
    password = 'password'
    receiver = 'email@email.com'
    body = 'Hello World!'

    yagmail.SMTP(from_,password).send(to = receiver,subject = 'random subject',contents = body)
    tkm.showinfo("Mail sent.")


def write_user_info_into_database():
    tkm.showinfo("Message",f"Your Data was saved to the Data Base! \n Now close the 'create account' window and press 'Login to your Penguin Mail Account' on the Main Page \n Fill in the form and then press 'Login'")


def user_forgot_username_or_password():
    pass

def check_user_data():
    #The code will be here
    #this function checks that data entered by the user is right
    tkm.showinfo("Message","You have Logged in ! \n Now close the Login window and Press on Compose in the menu")

def create_acc():
    global entry_name

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
    #button_create_acc = tk.Button(window_create_acc,text=f'Create a {mail_client_name} Account',font=("Arial",16),command=write_user_info_into_database,fg='green')
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

def login():
    global entry_username_login

    window_login=tk.Tk()
    window_login.title(f"{mail_client_name} - Login Page")
    window_login.geometry("350x190")
    window_login.resizable(False,False)
    window_login.configure(bg='#F16767')
    
    #Text boxes
    entry_username_login = tk.Entry(window_login,width=29,font=("Arial",13))
    entry_username_login.place(x=90,y=0)
    entry_password = tk.Entry(window_login,width=29,font=("Arial",13))
    entry_password.place(x=90,y=50)

    def clear_all_text_fields_window_login_func():
        entry_username_login.delete(0,"end")
        entry_password.delete(0,"end")

    #Buttons
    button_login = tk.Button(window_login,text='Login',font=("Arial",16),command=check_user_data,fg='green')
    button_login.place(x=150,y=140)
    button_forgot = tk.Button(window_login,text='Forgot Username or Password',font=("Arial",16),command=user_forgot_username_or_password,fg='green')
    button_forgot.place(x=70,y=95)
    button_clear_all_text_fields_window_login = tk.Button(window_login,text='Clean Text Fields',font=("Arial",11),command=clear_all_text_fields_window_login_func,fg='green')
    button_clear_all_text_fields_window_login.place(x=0,y=160)


    #Label
    label_username=tk.Label(window_login,text="Username",font=("Arial",16))
    label_username.place(x=0,y=0)
    label_password=tk.Label(window_login,text="Password",font=("Arial",16))
    label_password.place(x=0,y=50)

def compose_email():
    window_compose=tk.Tk()
    window_compose.title(f"{mail_client_name} - Email Composing Page")
    window_compose.geometry("500x600")
    window_compose.resizable(False,False)
    window_compose.configure(bg='#497E76')

    #Text boxes
    entry_receiver = tk.Entry(window_compose,width=65,font=("Arial",13))
    entry_receiver.place(x=90,y=50)
    entry_subject = tk.Entry(window_compose,width=65,font=("Arial",13))
    entry_subject.place(x=90,y=100)
    text_body=tk.Text(window_compose,wrap="word")
    text_body.place(x=0,y=195,relheight=0.5,relwidth=1)

    def clear_all_text_fields_window_compose_func():
        entry_receiver.delete(0,"end")
        entry_subject.delete(0,"end")
        text_body.delete(1.0,"end")

    #Buttons
    button_send_email = tk.Button(window_compose,text='Send Email',font=("Arial",19),command=send_mail,fg='green')
    button_send_email.place(x=45,y=520)
    button_clear_all_text_fields_window_compose = tk.Button(window_compose,text='Clean Text Fields',font=("Arial",19),command=clear_all_text_fields_window_compose_func,fg='green')
    button_clear_all_text_fields_window_compose.place(x=250,y=520)

    #Label
    label_account_info=tk.Label(window_compose,text=f"Sender's Username : {entry_username_login}",font=("Arial",16))
    label_account_info.place(x=140,y=0)

    label_receiver=tk.Label(window_compose,text="To",font=("Arial",16))
    label_receiver.place(x=0,y=50)
    label_subject=tk.Label(window_compose,text="Subject",font=("Arial",16))
    label_subject.place(x=0,y=100)
    label_body=tk.Label(window_compose,text="Body",font=("Arial",16))
    label_body.place(x=0,y=150)

#Menu
main_menu=tk.Menu(window_welcome)
window_welcome.configure(menu=main_menu)
mail_client_menu=tk.Menu(main_menu)


main_menu.add_cascade(label="Compose",menu=mail_client_menu)
mail_client_menu.add_command(label="New Email",command=compose_email)

#Text Fields


#Buttons
#Main page
button_create_acc = tk.Button(window_welcome,text=f'Create a {mail_client_name} Account',font=("Arial",16),command=create_acc,fg='green')
button_create_acc.place(x=70,y=60)
button_login = tk.Button(window_welcome,text=f'Login to your {mail_client_name} Account',font=("Arial",16),command=login,fg='green')
button_login.place(x=55,y=150)

#Labels
#Main page
label_welcoming_the_user=tk.Label(window_welcome,text=f"Welcome to {mail_client_name} !",font='Helvetica 18 bold')
label_welcoming_the_user.place(x=80,y=10)
label_or=tk.Label(window_welcome,text="or",font='Helvetica 18 bold')
label_or.place(x=175,y=105)


window_welcome.mainloop()


'''from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()'''




#https://support.google.com/accounts/answer/185833?visit_id=637966989204743938-2155131695&p=InvalidSecondFactor&rd=1 