def decrement(numbers):
    antalTal = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            numbers[i] = numbers[i]-1
            antalTal += 1
    return antalTal


tal = [9, 4, -8, -5, 0, 2]
nb = decrement(tal)
print(tal) # [8, 3, -8, -5, 0, 1]
print(nb) # 3