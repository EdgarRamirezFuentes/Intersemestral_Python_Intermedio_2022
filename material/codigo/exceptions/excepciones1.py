def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except TypeError:
        print("No se pueden usar caracteres")

resultado = divide(10,'a')
print(resultado)
