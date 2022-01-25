import sqlite3

def create_user_table():
    conn = sqlite3.connect('client.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE usuario (id_user int, name varchar, age int, height int, id text);')
    conn.commit()
    conn.close()

# create_user_table()

def add_user(data):
    conn = sqlite3.connect('client.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuario (id_user, name, age, height, id) VALUES ({}, "{}", {}, {}, "{}");'.format(data[0], data[1], data[2], data[3], data[4]))
    conn.commit()
    conn.close()


data = [1, "Edgar", 23, 1.75, 'id.pdf']

# add_user(data)

def get_data():
    conn = sqlite3.connect('client.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuario;')
    data = cursor.fetchall()  
    print(data)


def delete_data(id):
    conn = sqlite3.connect('client.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuario WHERE id_user = {};'.format(id))
    conn.commit()
    conn.close()


get_data()  
delete_data(1)
get_data()