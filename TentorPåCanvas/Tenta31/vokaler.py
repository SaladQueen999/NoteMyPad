ord = input("Skriv ett ord: ")
vokaler = "aouåeiyäö"
nytt_ord = ""
for i in range(len(ord)):
    if ord[i].lower() in vokaler:
        nytt_ord += ord[i].lower()
        nytt_ord += ord[i].upper()
        nytt_ord += ord[i].lower()
    elif ord[i] not in vokaler:
        nytt_ord += ord[i]

print(nytt_ord)