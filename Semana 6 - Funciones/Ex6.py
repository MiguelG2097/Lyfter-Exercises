def alphabetic_string():
    string = input ("Insert word: ")
    result = string.split("-")
    result.sort()
    string_sorted = "-".join(result)
    print(string_sorted)
    return string_sorted

alphabetic_string()


    