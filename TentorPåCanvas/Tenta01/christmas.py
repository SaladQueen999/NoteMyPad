dag = int(input("Dag: "))
månad = input("Månad: ")
periodNov = 54
periodDec = 23
if månad == "november":
    dagarKvar = periodNov - dag
    if dagarKvar > 1:
        print(f'Det är {dagarKvar} dagar kvar till julafton')
    else:
        print(f'Det är 1 dag kvar till julafton')
elif månad == "december":
    dagarKvar = periodDec - dag
    if dagarKvar > 1:
        print(f'Det är {dagarKvar} dagar kvar till julafton')
    else:
        print(f'Det är 1 dag kvar till julafton')