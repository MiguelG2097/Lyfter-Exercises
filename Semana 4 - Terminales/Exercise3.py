number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Ingrese el terver numero: "))

if number1 >= number2 and number1 >= number3:
    mayor = number1
elif number2 >= number1 and number2 >= number3:
    mayor = number2
else:
    mayor = number3

print(f"El numero mayor es: {mayor}")