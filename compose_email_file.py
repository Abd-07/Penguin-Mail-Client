import tkinter as tk
from send_mail_file import send_mail
import login_file
import check_user_data_file

import login_file

mail_client_name = "Penguin Mail"

entry_receiver = None
entry_subject = None
text_body = None
c_user_name = None

def clear_all_text_fields_window_compose_func():
    pass

def compose_email():
    global entry_receiver,entry_subject,text_body, c_user_name

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

    #Buttons
    button_send_email = tk.Button(window_compose,text='Send Email',font=("Arial",19),command=send_mail,fg='green')
    button_send_email.place(x=45,y=520)
    button_send_email["command"] = lambda send_button = button_send_email : send_mail()
    button_clear_all_text_fields_window_compose = tk.Button(window_compose,text='Clean Text Fields',font=("Arial",19),command=clear_all_text_fields_window_compose_func,fg='green')
    button_clear_all_text_fields_window_compose.place(x=250,y=520)

    #Label
    c_user_name = check_user_data_file.string_user_name
    label_account_info=tk.Label(window_compose,text=f"Sender's Username in Penguin Mail: {check_user_data_file.string_user_name}",font=("Arial",16))
    label_account_info.place(x=140,y=0)

    label_receiver=tk.Label(window_compose,text="To",font=("Arial",16))
    label_receiver.place(x=0,y=50)
    label_subject=tk.Label(window_compose,text="Subject",font=("Arial",16))
    label_subject.place(x=0,y=100)
    label_body=tk.Label(window_compose,text="Body",font=("Arial",16))
    label_body.place(x=0,y=150)