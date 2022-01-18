def divide(x,y):
    try:
        operacion =  x/y
    except (ZeroDivisionError,TypeError) :
        print("No se puede dividir entre cero y no se aceptan caracteres")
    else:
        resultado2 = operacion/'a'
        return operacion
    finally:
        print("Gracias por usar la herramienta division")
        print("Si jala")

resultado = divide(10,2)
print(resultado)


