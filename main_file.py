import tkinter as tk

from compose_email_file import compose_email
from create_acc_file import create_acc
from login_file import login
import send_mail_file

mail_client_name = "Penguin Mail"

window_welcome = tk.Tk()
window_welcome.title(f"{mail_client_name} - Main Page")
window_welcome.geometry("400x210")
window_welcome.resizable(False,False)
window_welcome.configure(bg='#E4A010')

entry_name_login = None
entry_name = None
entry_surname = None
entry_username_create_acc = None
entry_password_penguin_mail = None
entry_email_address = None
entry_email_password = None

entry_username_login = None
entry_password = None

#Menu
main_menu=tk.Menu(window_welcome)
window_welcome.configure(menu=main_menu)
mail_client_menu=tk.Menu(main_menu)


main_menu.add_cascade(label="Compose",menu=mail_client_menu)

mail_client_menu.add_command(label="New Email",command=lambda menu_button = mail_client_menu : compose_email())

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

#https://support.google.com/accounts/answer/185833?visit_id=637966989204743938-2155131695&p=InvalidSecondFactor&rd=1 


