


def prime_check(num:int):
    if num < 2:
        return
    isPrime = True
    for i in range(2,num):
        if num % i == 0:
            isPrime = False
            break
    if(isPrime):
        return num
    
lst = [1,2, 3, 5, 11, 17, 23, 31, 8, 12, 20, 25, 32, 41, 54, 60]
new_lst = list(filter(prime_check,lst))
print(new_lst)

