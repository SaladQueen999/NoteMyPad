def swap_case(string):
    nya_ordet = ""
    if string == "":
        raise ValueError("Error!")
    for i in range(len(string)):
        if string[i].isupper():
            nya_ordet += string[i].lower()
        elif string[i].islower():
            nya_ordet += string[i].upper()
    return nya_ordet

print(swap_case('JSON-fil'))