# Memorizzare una serie di numeri presi in input dall’utente.
# Memorizzare un ulteriore numero preso in input dall’utente.
# Mostrare se il numero è presente nella serie.
# Variante: mostrare quante volte il numero compare nella serie

# chiedere lunghezza lista
while True:  # ciclo di controllo input
    try:
        lenLista = int(input("Quanti numeri vuoi inserire dentro le liste? "))  # chiedo la lungezza della lista
    except ValueError:  # eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

# compilo lista 1 (altezza)
l1 = []  # creo una lista
for i in range(lenLista):  # ciclo for per inserire dentro la lista n valori decisi da utente
    while True:  # ciclo di controllo input
        try:
            num = float(input("Insersci un numero: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    l1.append(num)  # inserisco il numero dentro la lista

# chiedere un numero
while True:  # ciclo di controllo input
    try:
        n = int(input("Inserisci un numero da memorizzare: "))  # chiedo la lungezza della lista
    except ValueError:  # eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

# controllo di n dentro la lista
if n in l1:
    sum = 0
    for i in l1:  # conto quante volte compare n dentro la lista
        if n == i:
            sum = sum + 1
    print("Il numero", n, "è presente", sum, "volta/e nella lista", l1)
else:
    print("Il numero", n, "NON è presente nella lista", l1)
