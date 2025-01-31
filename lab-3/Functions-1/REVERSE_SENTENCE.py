
def reversed_string(string:str):
    splitted = string.split()
    splitted.reverse()
    new_string = ""
    for x in splitted:
        new_string += x
        new_string += " "
    return new_string

print(reversed_string("I'm new to Python"))