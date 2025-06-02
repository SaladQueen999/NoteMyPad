def find_longest_pos(lista):
    indexOfLongest = 0
    longest = 0
    for i in range(len(lista)):
        if len(lista[i]) >= longest:
            longest = len(lista[i])
            indexOfLongest = i
    return indexOfLongest


print(find_longest_pos(['en', 'mycket', 'lång', 'text']))