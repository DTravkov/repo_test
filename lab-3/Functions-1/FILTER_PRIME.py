
def filter_prime(nums:list):
    primes = []
    for i in nums:
        if(i == 1):
            continue
        isPrime = True
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    return primes



