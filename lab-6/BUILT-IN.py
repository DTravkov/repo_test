import time,math




def list_multiply(lst):
    return math.prod(lst)
print(list_multiply([1,2,3,4,5]))


def upper_count(string):
    up_count = sum(1 for x in string if x.isupper())
    low_count = sum(1 for x in string if x.islower())
    return up_count,low_count

print(upper_count("ABABababab"))



def ispalindrome(string):
    return string == string[::-1]
    
print(ispalindrome("radar"))


def delay_root(num,delay):
    time.sleep(delay/1000)
    return f"Square root of {num} is {math.sqrt(num)} after {delay} miliseconds"

print(delay_root(400,500))

def istruetuple(tple):
    return all(tple)

tple = (1,"a")
print(istruetuple(tple))