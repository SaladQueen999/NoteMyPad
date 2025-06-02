def emphasize(sentence):
    nytt_ord = ""
    nytt_ord += sentence[0].upper()
    for i in range(1,len(sentence)-1):
        if sentence[i-1] == " ":
            nytt_ord += sentence[i].upper()
        elif sentence[i-1] == " ":
            nytt_ord += sentence[i].lower()
            nytt_ord += "."
        else:
            nytt_ord += sentence[i].lower()
    return nytt_ord


print(emphasize('I REALLY need coffee.'))
# I. Really. Need. Coffee.

# NOT SOLVED