array1 = ["A", "A", "A"]
array2 = ["B", "B", "B"]

array3 = ["C", "C", "C", "C"]
array4 = ["D"]

def shuffle(a1, a2):
    out = []
    min_array = min(len(a1), len(a2))
    for i in range(0, min_array):
        out.append(a1[i])
        out.append(a2[i])

    out.extend(a1[min_array:] or a2[min_array:])
    return out

print(shuffle(array1, array2))
print(shuffle(array3, array4))