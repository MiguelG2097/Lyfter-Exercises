def menu_calc():
    current_value = 0

    
    while True:
        try:
            print("Seleccione un valor para realizar la operacion: ")
            print("1- Suma")
            print("2- Resta")
            print("3- Multiplicacion")
            print("4- Division")
            print("5- Borrar Resultado")
            print("6- Salir")

            num = int(input("Ingrese el numero para proceder con la operacion: "))
            print(f"El numero actual es: {current_value}")

            if num == 1:
                result = sum_num(current_value)
                print("El resultado de la suma es de: ", result)
                current_value = result 
                print(current_value)
            elif num == 2:
                result = substraction(current_value)
                print("El resultado de la resta es de: ", result)
                current_value = result 
                print(current_value)
            elif num == 3:
                result = multiplication(current_value)
                print("El resultado de la multiplicacion es de: ", result)
                current_value = result 
                print(current_value)
            elif num == 4:
                result = division(current_value)
                print("El resultado de la division es de: ", result)
                current_value = result 
                print(current_value)
            elif num == 5:
                (borrar_resultado)
                current_value = borrar_resultado()
                print("El numero actual es: ", current_value)
            elif num == 6:
                print("Saliendo de la calculadora ")
                break
            else:
                print("Opcion incorrecta. Seleccione una opcion del menu.")
        except ValueError as error:
            print(f"La opcion seleccionada es incorrecta. Seleccione un numero del menu")

def sum_num(current_value):

    sum_num1 = int(input("Ingrese el numero a sumar: "))
    return current_value + sum_num1
    

def substraction(current_value):

    sub_num1 = int(input("Ingrese el numero a restar: "))
    return current_value - sub_num1

def multiplication(current_value):
    mul_num1 = int(input("Ingrese el numero a multiplicar: "))
    return current_value * mul_num1

def division(current_value):
    div_num1 = int(input("Ingrese el numero a dividir: "))
    return current_value / div_num1

def borrar_resultado():
    print("Resultado ha sido borrado ")
    return 0


menu_calc()