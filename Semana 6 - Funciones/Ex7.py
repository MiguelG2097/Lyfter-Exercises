import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers():
    numbers = []
    num = int(input("Cuantos numeros desea ingresar? "))

    for i in range(num):
        num_ask = int(input(f"Ingrese el numero {i+1}: "))
        numbers.append(num_ask)
    
    primes = []
    for i in numbers:
        if is_prime(i):
            primes.append(i)
    print("Los numeros primos son: ",primes)

prime_numbers()

