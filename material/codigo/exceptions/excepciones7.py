def divide(x,y):
    try:
        operacion =  x/y       
    except (ZeroDivisionError) :
        print("No se puede dividir entre cero")
        try:
            resultado2 = 10/'b'
        except TypeError:
            print("Fatal error dentro del segundo bloque try")
    else:
        #resultado2 = operacion/'a'
        return operacion
    finally:
        print("Gracias por usar la herramienta division")
        print("Si jala")

resultado = divide(10,0)
print(resultado)


