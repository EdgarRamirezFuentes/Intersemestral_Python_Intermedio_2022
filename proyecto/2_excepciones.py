'''
    Name: 2_excepciones.py
    Description: Get the BMI and the status based on the BMI
    Author: Edgar Alejandro Ramírez Fuentes
    Date: 01/23/2021
'''

import sys

def get_BMI(height : float, weight : float):
    '''
        Get the body mass index based on the height and weight

        Parameters
        --------------

        height : float
            It is the height of the person

        weight : float
            It is the weight of the person

        Return
        ---------------

        bmi : float
            It is the BMI of the person
    '''
    try:
        if height <= 0 or weight <= 0:
            raise ValueError('The values must be greater than 0')
        bmi = weight / height**2
    except ArithmeticError as e:
        sys.exit(f'Error: {e}')
    except TypeError as e:
        sys.exit(f'Error: {e}')
    except ValueError as e:
        sys.exit(f'Error: {e}')
    except Exception as e:
        sys.exit(f'Error: {e}')
    else:
        return bmi


def get_BMI_status(bmi : float):
    '''
        Get the BMI status based on the received BMI

        Paramaters
        ------------

        bmi : float

        Return
        ------------
        status : str
            It is the current BMI status
    
    '''
    try:
        status = ''
        if bmi <= 0:
            raise ValueError('Invalid BMI')
        elif bmi < 18.5:
            status = 'Bajo peso'
        elif bmi >= 18.5 and bmi <= 24.9:
            status = 'Saludable'
        else:
            status = 'Sobrepeso' 
    except TypeError as e:
        sys.exit(f'Error: {e}')
    except ValueError as e:
        sys.exit(f'Error: {e}')
    except Exception as e:
        sys.exit(f'Error: {e}')
    else:
        return status


if __name__ == "__main__":
    # Getting the height
    try:
        height = float(input("Height (m): "))
        if height < 0:
            raise ValueError('The height must be greater than 0')
    except TypeError as e:
        sys.exit(f'Error: {e}')
    except ValueError as e:
        sys.exit(f'Error: {e}')
    except Exception as e:
        sys.exit(f'Error: {e}')

    # Getting the weight
    try:
        weight = float(input("Weight (kg): "))
        if weight < 0:
            raise ValueError('The weight must be greater than 0')
    except TypeError as e:
        sys.exit(f'Error: {e}')
    except ValueError as e:
        sys.exit(f'Error: {e}')
    except Exception as e:
        sys.exit(f'Error: {e}')

    bmi = get_BMI(height, weight)
    status = get_BMI_status(bmi)
    print(f'BMI: {bmi} Status: {status}')

    pass
