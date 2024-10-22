import sqlite3

connection = sqlite3.connect("module 14/initiate.db")
curs = connection.cursor()

curs.execute('''
CREATE TABLE IF NOT EXISTS Product(
id INT,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
)
''')

for i in range(1, 5):
    curs.execute("INSERT INTO Product (id, title, description, price ) VALUES (?, ?, ?, ?)", (f"{i}", f"Продукт{i}", f"Описание{i}", f"{i * 100}"))

def get_all_products(id, title, description, price):
    full = [id, title, description, price]
    return full

connection = sqlite3.connect("module 14/initiate.db")
curs = connection.cursor()

curs.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMACY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL
)
''')

def add_user(username, email, age):
    curs.execute(f'INSERT INTO Users VALUES({username},{email},{age}, {1000})')

def is_included(username):
    only_username = curs.execute('INSERT INTO Users (username) VALUES(?)', (f'{username}',))
    if only_username.fetchone() is None:
        return False


connection.commit()
connection.close()




    #if check_user.fetchone() is None:
        #curs.execute(f'''
    #INSERT INTO Users VALUES('{username}','{email}f','{age}', 1000)
    #''')
    #else:
        #return False
    #connection.commit()
