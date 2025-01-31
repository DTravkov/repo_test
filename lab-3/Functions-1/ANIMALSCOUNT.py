def solve(numheads,numlegs):
    if numlegs < numheads * 2 or numlegs > numheads * 4 or (numlegs % 4 != 0 and numlegs % 2 != 0):
        return "Impossible"
    
    chickens = 0
    rabbits = 0

    lst = list([2 for x in range(numheads)])

    if sum(lst) < numlegs:
        i = -1
        while sum(lst) < numlegs:
            lst[i] += 2
            i -= 1
    
            

    for x in lst:
        if x == 2:
            chickens += 1
        elif x == 4:
            rabbits += 1
    return f"Chickens: {chickens} , Rabbits : {rabbits}.\nChecking values  :\nInitial amount of legs = {numlegs}.\nAmount of legs in our calculation ({chickens} * 2 + {rabbits} * 4) = {chickens * 2 + rabbits * 4}.\nIn ths case my solution is {chickens * 2 + rabbits * 4 == numlegs}"
    



print(solve(35,94))