import tkinter as tk
from check_user_data_file import check_user_data
from user_forgot_username_or_password_file import user_forgot_username_or_password

mail_client_name = "Penguin Mail"

entry_username_login = None
entry_password = None

def login():
    global entry_username_login,entry_password

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
    button_login["command"] = lambda check_button = button_login : check_user_data()
    button_forgot = tk.Button(window_login,text='Forgot Username or Password',font=("Arial",16),command=user_forgot_username_or_password,fg='green')
    button_forgot.place(x=70,y=95)
    button_clear_all_text_fields_window_login = tk.Button(window_login,text='Clean Text Fields',font=("Arial",11),command=clear_all_text_fields_window_login_func,fg='green')
    button_clear_all_text_fields_window_login.place(x=0,y=160)


    #Label
    label_username=tk.Label(window_login,text="Username",font=("Arial",16))
    label_username.place(x=0,y=0)
    label_password=tk.Label(window_login,text="Password",font=("Arial",16))
    label_password.place(x=0,y=50)