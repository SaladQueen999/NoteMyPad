plockade = int(input("antal plockade: ")) #16
perLåda = int(input("Per Låda: ")) #6
kvar = plockade % perLåda #4
if kvar != 0:
    print (f'Antal äpplen kvar att plocka {perLåda - kvar}')
else:
    print ("Antal äpplen kvar att plocka: 0")
