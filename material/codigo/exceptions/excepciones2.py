def divide(x,y):
    try:
        return x/y
    except (ZeroDivisionError,TypeError) :
        print("No se puede dividir entre cero y no se aceptan caracteres")

resultado = divide(10,0)
print(resultado)

