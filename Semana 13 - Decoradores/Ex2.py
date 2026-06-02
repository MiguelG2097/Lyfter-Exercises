def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for argument in args:
            if not isinstance(argument, (int, float)):
                raise ValueError("Los parametros deben ser numeros")

        for argument in kwargs.values():
            if not isinstance(argument, (int, float)):
                raise ValueError("Los parametros deben ser numeros")

        return func(*args, **kwargs)

    return wrapper


@validate_numbers
def multiply_numbers(a, b):
    return a * b


print(multiply_numbers(5, 4))