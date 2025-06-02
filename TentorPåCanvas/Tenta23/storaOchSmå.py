ord = input("Skriv ett ord: ")
stora = input("Bokstäver att göra stora: ")
nytt_ord = ""
for bokstav in ord:
    if bokstav in stora:
        nytt_ord += bokstav.upper()
    else:
        nytt_ord += bokstav
print(nytt_ord)