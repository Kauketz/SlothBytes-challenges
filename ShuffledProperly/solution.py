
def isShuffledWell(array):
    for j in range(1, len(array)-1):
        if array[j-1] + 1 == array[j] and array[j+1] == array[j]+1:
            return False
        if array[j-1] - 1 == array[j] and array[j+1] == array[j]-1:
            return False
    return True


print(isShuffledWell([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))  # False
print(isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))  # False
print(isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))  # True
print(isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))  # True
