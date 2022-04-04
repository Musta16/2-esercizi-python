# Memorizzare due serie di numeri presi in input dall’utente.
# Mostrare se le due serie hanno almeno un elemento in comune.
# 1. Solo con liste - 2. Solo con set

# chiedere lunghezza liste
while True:  # ciclo di controllo input
    try:
        lenLista1 = int(input("Quanti numeri vuoi inserire dentro la prima lista? "))  # chiedo la lungezza della lista
        lenLista2 = int(
            input("Quanti numeri vuoi inserire dentro la seconda lista? "))  # chiedo la lungezza della lista
    except ValueError:  # eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

# compilo lista 1 (altezza)
l1 = []  # creo una lista
for i in range(lenLista1):  # ciclo for per inserire dentro la lista n valori decisi da utente
    while True:  # ciclo di controllo input
        try:
            num = float(input("Insersci un numero: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    l1.append(num)  # inserisco il numero dentro la lista

# compilo lista 1 (altezza)
l2 = []  # creo una lista
for i in range(lenLista2):  # ciclo for per inserire dentro la lista n valori decisi da utente
    while True:  # ciclo di controllo input
        try:
            num = float(input("Insersci un numero: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    l2.append(num)  # inserisco il numero dentro la lista

# 1. Solo con liste
numComuni = []
comuni = False
for i in l1:
    if i in l2:
        comuni = True
        numComuni.append(i)
if comuni is True:
    print("Le due liste hanno in comune:", numComuni)
else:
    print("Non ci sono numeri in comune!")

# 2. Solo con set

s1 = set(l1)
s2 = set(l2)
if len(s1 & s2) == 0:
    print("Non ci sono numeri in comune!")
else:
    print("Le due liste hanno in comune:", s1 & s2)
