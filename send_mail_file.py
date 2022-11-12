import yagmail
import tkinter.messagebox as tkm

import compose_email_file
import database
import login_file

def send_mail():
    
    from_ = database.get_email_by_name(compose_email_file.c_user_name)
    password = str(database.get_db_username_pass_email(compose_email_file.c_user_name, flag = False))
    receiver = str(compose_email_file.entry_receiver.get())
    body = compose_email_file.text_body.get("1.0","end")
    subject_ = compose_email_file.entry_subject.get()

    yagmail.SMTP(from_,password).send(to = receiver,subject = subject_,contents = body)
    tkm.showinfo("Alert","Mail sent.")