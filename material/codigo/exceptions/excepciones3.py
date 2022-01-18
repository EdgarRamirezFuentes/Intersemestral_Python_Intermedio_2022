def divide(x,y):
    try:
        operacion =  x/y
    except (ZeroDivisionError,TypeError) :
        print("No se puede dividir entre cero y no se aceptan caracteres")
    else:
        return operacion 

resultado = divide(10,0)
print(resultado)

