def hitta_sekvens(lista):
    if len(lista) < 2:
        raise ValueError("Error!")

    längsta_sekvens = 1
    temp = 1
    största = lista[0]

    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1]:
            temp += 1
            if temp > längsta_sekvens:
                längsta_sekvens = temp
                största = lista[i]
        else:
            temp = 1

    return största


lst = [4, 4, 9, 12, 12, 12, 4, 4]
print(hitta_sekvens(lst)) # 12