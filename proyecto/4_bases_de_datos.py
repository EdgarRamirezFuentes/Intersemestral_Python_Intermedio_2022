'''
    Name: 4_bases_de_datos.py
    Description: Basic CRUD in python using sqlite3
    Author: Edgar Alejandro Ramírez Fuentes
    Date: 01/24/2021
'''

import sqlite3
import sys

def create_users_table():
    '''
        Create the database with the table users
    '''
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE user (id_user int, name varchar, age int, height int, id text);')
        conn.commit()
        conn.close()
    except Exception as e:
        sys.exit(f'Error: {e}')


def add_user(user_data : list):
    '''
        Add a new user to the  database

        Parameters
        --------------

        user_data : list 
            It is a list that contains the data to register in the database
    '''
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user (id_user, name, age, height, id) VALUES ({}, "{}", {}, {}, "{}");'.format(user_data[0], # id
                                                                                                                    user_data[1], # name
                                                                                                                    user_data[2], # age
                                                                                                                    user_data[3], # height
                                                                                                                    user_data[4])) #id
        conn.commit()
        conn.close()
    except Exception as e:
        sys.exit(f'Error: {e}')


def get_data():
    '''
        Get all the rows in the database

        Return
        -------

        data : list
            It is a list that contains each row in the database
    '''
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user;')
        data = cursor.fetchall()  
    except Exception as e:
        sys.exit(f'Error: {e}')
    else:
        return data


def delete_data(user_id : int):
    '''
        Delete an user from the database using their id

        Parameters
        -----------

        user_id
            It is the id that will be deleted from the database
    '''
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM user WHERE id_user = {};'.format(user_id))
        conn.commit()
        conn.close()
    except Exception as e:
        sys.exit(f'Error: {e}')


def update_data(user_id : int, height : float, id : str):
    '''
        Update the height and id information for the row with the received id

        Parameters
        -----------

        user_id : int
            It is the user_id
        
        height : float
            It is the height value that will be updated

        id : str
            It is the id value that will be updated
    '''
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE user SET height = {}, id = "{}" WHERE id_user  = {};'.format(height, id, user_id))
        conn.commit()
        conn.close()
    except Exception as e:
        sys.exit(f'Error: {e}')


people = [
    [1, "Edgar", 23, 1.75, 'id_edgar.pdf'],
    [2, "Yael", 24, 1.70, 'id_yael.pdf'],
    [3, "Ivan", 22, 1.70, 'id_ivan.pdf'],
    [4, "Tony", 25, 1.74, 'id_tony.pdf'],
    [5, "Rodolfo", 23, 1.70, 'id_rodolfo.pdf'],
]



if __name__ == "__main__":
    # Creating the database
    create_users_table()

    # Adding users to our table users
    for person in people:
        add_user(person)

    # Getting the current data in the database
    users = get_data()  
    print(users)

    # Deleting the last user added
    delete_data(4)
    delete_data(5)

    # Getting the current data in the database
    users = get_data()  
    print(users)

    # Updating two users
    update_data(1, 1.76, 'id_Edgar_ramirez.pdf')

    # Getting the current data in the database
    users = get_data()  
    print(users)

