import sqlite3

connection = sqlite3.connect("module 14/initiate2.db")
curs = connection.cursor()


def initiate_db():
    curs.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMACY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL)
    ''')
    curs.execute('''
    CREATE TABLE IF NOT EXISTS Product(
    id INT PRIMACY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL)
    ''')
    connection.commit()


initiate_db()

curs.execute('DELETE FROM Product')
for i in range(1, 5):
    curs.execute("INSERT INTO Product (id, title, description, price ) VALUES (?, ?, ?, ?)",
                 (f"{i}", f"Продукт{i}", f"Описание{i}", f"{i * 100}"))
    connection.commit()


def get_all_products(id, title, description, price):
    full = [id, title, description, price]
    return full


def add_user(username, email, age):
    curs.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, 1000)', (username, email, age))
    connection.commit()


def is_included(username):
    curs.execute('SELECT * FROM Users')
    users = curs.fetchall()
    for i in users:
        if i[1] == username:
            return True
    return False
