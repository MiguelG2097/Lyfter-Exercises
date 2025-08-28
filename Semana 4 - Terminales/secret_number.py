import random

# Generar número secreto entre 1 y 10
secret_number = random.randint(1, 10)

# Mensaje inicial
print("¡Adivina el número secreto entre 1 y 10!")

# Bucle hasta que el usuario adivine
while True:
    try:
        number = int(input("Ingrese su intento: "))
        
        if number == secret_number:
            print("¡Felicidades! Adivinaste el número secreto.")
            break
        else:
            print("Número incorrecto. Intenta nuevamente.")
    except ValueError:
        print("Por favor, ingresa un número válido.")