def print_params_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Parámetros posicionales: {args}")
        print(f"Parámetros nombrados: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Retorno de la función: {result}")

        return result

    return wrapper


@print_params_and_return
def sum_numbers(a, b):
    return a + b


result = sum_numbers(10, 5)

print(f"Resultado final: {result}")