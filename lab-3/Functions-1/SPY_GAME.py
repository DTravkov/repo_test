

def spy_game(nums:list):
    if nums == None:
        return False
    if(len(nums) < 3):
        return False
    check = []
    for x in nums:
        if x == 0 or x == 7:
            check.append(x)

    i = 0
    j = 2
 
    while j <= len(check):
        if check[i:j+1] != [0,0,7]: 
            i += 1
            j += 1
        else: 
            return True
    
    return False
    
print(spy_game([7,0,0,3,5]))
print(spy_game([3,0,4,0,4,3,1,4,7]))