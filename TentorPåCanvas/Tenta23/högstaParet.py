def hitta_par(lista):
    störstaParet = 0
    if len(lista) < 2:
        raise ValueError("Error, färre än 2 element!")
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            if lista[i] > störstaParet:
                störstaParet = lista[i]
    return störstaParet
            
tal = [12, 25, 12, 11, 25, 25, 23, 36, 10]
print(hitta_par(tal)) # 25