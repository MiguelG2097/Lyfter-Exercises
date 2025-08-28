## Variable Global ##

number = 10

def sum():
    global number
    number = 5
    sum = 10 + number
    print(sum)

sum()

## ------------------------- ##

## Variable Local ##


def printing():
    number = 5 
    print(f'This is the number: ',number)

printing()