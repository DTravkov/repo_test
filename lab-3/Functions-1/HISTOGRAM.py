
def histogram(lst:list):
    for x in lst:
        lst[lst.index(x)] = list(['*' for y in range(x)])
        
    for x in lst:
        print("".join(x))

histogram([6,5,4,3,2,1,2,3,4,5,6])