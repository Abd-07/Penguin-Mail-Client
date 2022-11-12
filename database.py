import email
from re import A
import sqlite3


DB_FILE_NAME = 'db.sqlite'

def create_connect():
    return sqlite3.connect(DB_FILE_NAME)

def init_db():
    with create_connect() as connect:
        connect.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id      INTEGER  PRIMARY KEY,
                name       STRING  NOT NULL,
                surname    STRING  NOT NULL,
                username       STRING  NOT NULL,
                password_penguin_mail    STRING  NOT NULL,
                email    STRING  NOT NULL,
                password_email    STRING  NOT NULL
            );
        ''')

        connect.commit()
init_db()       

def get_db_username_pass_peng_mail(username):
    conn = sqlite3.connect(DB_FILE_NAME)

    all_info_of_user_from_its_row = conn.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchone()

    if all_info_of_user_from_its_row is None:
        add_message(username)
        conn.close()
        
        return None
    
    else:
        conn.close()

        username = all_info_of_user_from_its_row[3]
        password = all_info_of_user_from_its_row[4]

        return username,password

def get_email_by_name(username):
    conn = sqlite3.connect(DB_FILE_NAME)

    all_info_of_user_from_its_row = conn.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchone()

    if all_info_of_user_from_its_row is None:

        return None
    
    else:
        conn.close()
        
        email = all_info_of_user_from_its_row[5]
        
        return email

def get_db_username_pass_email(username, flag=True):
    conn = sqlite3.connect(DB_FILE_NAME)
    
    all_info_of_user_from_its_row = conn.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchone()
    
    if all_info_of_user_from_its_row is None:
        add_message(username)
        conn.close()

        return None

    elif flag == False:
        conn.close()
        password_email = all_info_of_user_from_its_row[6]

        return password_email

    else:
        conn.close()
        email = all_info_of_user_from_its_row[5]
        password_email = all_info_of_user_from_its_row[6]
        
        return email,password_email


def add_message(name,surname,username,password_penguin_mail,email,password_email):
    with create_connect() as connect:
        connect.execute(
            'INSERT INTO Users(name, surname, username, password_penguin_mail, email, password_email) VALUES(?,?,?,?,?,?)', (name, surname, username, password_penguin_mail, email, password_email)
        )
        connect.commit()

def delete_message(id):
    with create_connect() as connect:
        connect.execute(
            f'DELETE FROM Users WHERE id={id}'
        )
        connect.commit()
