def divide(x,y):
    try:
        operacion =  x/y
        
        if operacion < 0:
            raise ValueError("No se aceptan numeros negativos") #1era

    except ValueError as numNegativo:
        print( numNegativo)
        
    except (ZeroDivisionError,TypeError) :
        print("No se puede dividir entre cero y no se aceptan caracteres")
    else:
        #resultado2 = operacion/'a'
        return operacion
    finally:
        print("Gracias por usar la herramienta division")
        print("Si jala")

resultado = divide(10,-2)
print(resultado)


