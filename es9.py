# memorizzare una serie di parole prese in input da utente
# memorizzare un numero preso da input utente
# costruire una nuova serie con solamente le parole più lunghe del numero
# soluzioni: 1. liste SENZA comprehension - 2. liste CON comprehension

# 1. liste SENZA comprehension

# chiedere lunghezza lista
while True:  # ciclo di controllo input
    try:
        lenLista = int(input("Quanti numeri vuoi inserire dentro le liste? "))  # chiedo la lungezza della lista
    except ValueError:  # eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

# compilo lista
l1 = []  # creo una lista
for i in range(lenLista):  # ciclo for per inserire dentro la lista n valori decisi da utente
    item = input("Insersci un numero: ")
    l1.append(item)

# chiedere un numero
while True:  # ciclo di controllo input
    try:
        n = int(input("Inserisci un numero da memorizzare: "))  # chiedo la lungezza della lista
    except ValueError:  # eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

listaNomiLunghi = []
for i in l1:
    if len(i) > n:
        listaNomiLunghi.append(i)

print("Lista nomi più lunghe di", n, "lettera/e:", listaNomiLunghi)

# 2. liste CON comprehension

listaComprehension = [i for i in l1 if (len(i) > n)]
print("Stessa cosa con il comprehension:", listaComprehension)
