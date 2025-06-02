def make_even(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            if numbers[i] < 0:
                numbers[i] = numbers[i]+1
            else:
                numbers[i] = numbers[i] -1
    return numbers


tal = [9, 4, -8, -5, 0, 2]
make_even(tal)
print(tal) # [8, 4, -8, -4, 0, 2]