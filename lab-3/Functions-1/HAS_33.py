


def has_33(nums:list):
    if nums == None:
        return False
    i = 0
    j = 2
    while j <= len(nums):
        if nums[i:j] != [3,3]:
            i += 1
            j += 1
        else:
            return True
    return False


print(has_33([3,0,3]))
print(has_33([3,2,3,4,3,3]))