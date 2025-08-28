def upper_lower_letters():

    string = input("Insert word: ")
    upper_count = 0
    lower_count = 0

    for i in string:
        if i.isupper():
            upper_count = upper_count + 1           
        elif i.islower():
            lower_count = lower_count + 1

    print(f"There is a total of {upper_count} upper letters and a total of {lower_count} lower letters")
    return(print)

upper_lower_letters()