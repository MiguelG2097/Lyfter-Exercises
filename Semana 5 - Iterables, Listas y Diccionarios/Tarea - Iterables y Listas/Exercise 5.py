list = []

for i in range (10):
    number = int(input('Enter a number: '))
    list.append(number)
    
max_number = max(list)
print(f'The max value entered is: ',max_number)