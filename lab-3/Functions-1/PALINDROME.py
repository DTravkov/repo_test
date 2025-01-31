
def isPalindrome(string:str):
    string = string.lower()
    string_reversed = list(string)
    string_reversed.reverse()
    string_reversed = "".join(string_reversed)
    if string == string_reversed:
        return True
    else:
        return False
    
print(isPalindrome(str(input("Enter your word..."))))