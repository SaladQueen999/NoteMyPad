def camel_to_snake(camel):
    nytt_ord = ""
    for i in range(len(camel)):
        if camel[i].isupper():
            nytt_ord += "_"
            nytt_ord += camel[i].lower()
        else:
            nytt_ord += camel[i]
    return nytt_ord


camel = input("Skirv ett cameCase: ")
print(camel_to_snake(camel))