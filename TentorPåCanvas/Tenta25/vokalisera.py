ord = input("Skriv ett ord: ")
nytt_ord = ""
vokaler = "aouåeiyäöAOUÅEIYÄÖ"
for i in range(len(ord)):
    if ord[i] in vokaler:
        nytt_ord += ord[i]*3
    else:
        nytt_ord += ord[i]
print(nytt_ord)
