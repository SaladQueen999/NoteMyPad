def max_difference(values):
    biggestDiff = 0
    for i in range(len(values)-1):
        diff = abs(values[i] - values[i+1])
        if diff > biggestDiff:
            biggestDiff = diff
    return biggestDiff

lst = [4, 6, 9, 12, 13, 9, 6]
print(max_difference(lst)) # 4