def unique(lst:list):

    unifier = {}

    i = 0
    while i < len(lst):
        unifier[lst[i]] = 1
        i += 1

    unified = [x for x in unifier.keys()]
    
    return unified

print(unique([3,2,6,7,1,1,3,2,4,5,6,5,7,7,7,7]))