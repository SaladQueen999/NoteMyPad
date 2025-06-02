barn = int(input("Antal barn: ")) #27
kakorPerBurk = int(input("Antal kakort per burk: ")) #4
delad = barn // kakorPerBurk
while delad * kakorPerBurk < barn:
    delad += 1
print(f"Antal burkar som behövs: {delad}")
