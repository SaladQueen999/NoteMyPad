tal = int(input("Ange ett tal: "))
divisors = 0
for i in range(1,tal):
    if tal % i == 0:
        divisors +=1
print (f'Antal divisorer: {divisors-1}')