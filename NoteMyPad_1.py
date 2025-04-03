#FRÅGA 4
lista = [12,13,14,15,25,25,6,73,26]
def hitta_par(lista):
    if len(lista) < 2:
        raise ValueError("Error! Less than 2")
    max_par = 0
    
    for i in range(len(lista) -1 ):
        if lista[i] == lista[i+1]:
            if lista[i] > max_par:
                max_par = lista[i]


    if max_par == 0:
        raise ValueError("Inga intilliggande par hittades")
    
    return max_par

#FRÅGA 5
numbers = [9, 4, -8, 0, -2, 2]
def decrement(numbers) :
    nb = 0
    for i in range(len(numbers)) :
        if numbers[i] > 0 :
            numbers[i] -=1
            nb +=1
    return nb

# Läs in ett heltal från användaren
tal = input('Skriv in ett heltal ')
# Multiplicera talet med 3 och skriv ut resultatet
print (tal * 3)