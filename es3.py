# Memorizzare due serie di numeri presi in input dall’utente. Mostrarne il prodotto scalare

import math

# chiedere lunghezza lista 1
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
            num = float(input("Insersci il valore dell'altezza: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    l1.append(num)  # inserisco il numero dentro la lista

# compilo lista 2 (base)
l2 = []  # creo una lista
for i in range(lenLista):  # ciclo for per inserire dentro la lista n valori decisi da utente
    while True:  # ciclo di controllo input
        try:
            num = float(input("Insersci il valore della base: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    l2.append(num)  # inserisco il numero dentro la lista

print("Lista altezza triangolo: ", l1)
print("Lista base triangolo: ", l2)

# calcolo la componente dell'altezza lungo la base
listaComponente = []
for i in l1:
    i = i/2
    listaComponente.append(i)

# calcolo il prodotto scalare
for i in range(lenLista):
    n = listaComponente[i] * l2[i]
    print("Risultato", i+1 , ":", n)