def snake_to_camel(snake):
    nytt_ord = ""
    i = 0
    for i in range(len(snake)):
        if snake[i] == "_":
            i += 1
            if i < len(snake):
                nytt_ord += snake[i].upper()
        else:
            nytt_ord += snake[i]
    return nytt_ord

snake = input("Skirv i snake_case: ")
print(snake_to_camel(snake))
