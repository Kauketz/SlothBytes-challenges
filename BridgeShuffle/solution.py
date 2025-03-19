
def bridgeShuffle(a1, a2):
    out = []
    min_array = min(len(a1), len(a2))
    for i in range(0, min_array):
        out.append(a1[i])
        out.append(a2[i])

    out.extend(a1[min_array:] or a2[min_array:])
    return out

print(bridgeShuffle(["A", "A", "A"], ["B", "B", "B"]))
print(bridgeShuffle(["C", "C", "C", "C"], ["D"]))
print(bridgeShuffle([1, 3, 5, 7], [2, 4, 6]))