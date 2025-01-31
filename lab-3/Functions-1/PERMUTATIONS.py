from itertools import permutations

def find_permutations(string):
    perm = permutations(string)
    return list(perm)

for x in find_permutations("abc"):
    print('\n')
    for y in x:
        print(y,end='')
    