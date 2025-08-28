list_number = [10, 20, 30, 40]

def sum_list(list_number):
    total_sum = 0
    for i in list_number:
         total_sum = total_sum + i

    print (f"The sum of the list is: ", total_sum)
    return total_sum

sum_list(list_number)


