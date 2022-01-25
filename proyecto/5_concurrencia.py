'''
    Name: 5_concurrencia.py
    Description: Using concurrent programming executed two functions
    Author: Edgar Alejandro Ramírez Fuentes
    Date: 01/24/2021
'''

from threading import Thread
import time


# Using Dynamic programming to improve the fibonacci function
dp = dict()


def count(last_number : int):
    '''
        Print from 0 to last_number 

        Parameters
        ------------

        last_numbers : int 
            It is the last number that will be printed
    '''
    try:
        if last_number <= 0:
            raise ValueError('The last number must be greater than 0')

        current_number = 0
        while current_number <= last_number:
            print(f'\nCount: {current_number}', end=' ')
            time.sleep(1.0)
            current_number += 1
    except Exception as e:
        print(f'Error: {e}')


def fibonacci(position : int):
    '''
        Print the fibonacci sequence until the desired position

        Parameters
        --------------
        position : int
            It is the position in the fibonacci sequence
    '''
    try:
        # Numbers less or equal than 0 are not valid
        if position <= 0:
            raise ValueError('The position must be greater than 0')

        # Return a value that has been already computed
        if dp.get(position):
            return dp[position]
        elif position < 3:
            # Print and register the base cases in the dp
            if not dp.get(position):
                dp[position] = 1
                print("1", end=" ")
            return 1
        elif (position - 1 > 0) and (position - 2 > 0):
            dp[position] = fibonacci(position - 2) + fibonacci(position - 1) 
            print(dp[position], end=" ")
            return dp[position]
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    fibonacci_thread = Thread(target=fibonacci, args=(40,))
    count_thread = Thread(target=count, args=(40,))
    # Start the threads
    fibonacci_thread.start()
    count_thread.start()
    # Wait until the count_thread finishes
    count_thread.join()
    print("Program finished")
