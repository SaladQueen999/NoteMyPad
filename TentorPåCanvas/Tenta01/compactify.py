text = input("Skirv en text: ")
nytt_ord = text[0]
for i in range(1, len(text)):
    if text[i] != text[i-1]:
        nytt_ord += text[i]
print(nytt_ord)