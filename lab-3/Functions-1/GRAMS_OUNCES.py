def ounces_to_gramms(grams):
    if type(grams) == int or type(grams) == float:
        return 28.3495231 * grams
    else:
        return "Invalid Input"

print(ounces_to_gramms(54))