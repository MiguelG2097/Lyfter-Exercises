import random

secret_number = random.randint(1,10)

while True:
    try:
        number = int(input("Ingrese el numero a adivinar: "))

        if number == secret_number:     
            print("Adivinaste el numero secreto")
            break
        else:
            print("Numero incorrecto")
    except ValueError:
        print("Por favor, ingresar numero valido")
    