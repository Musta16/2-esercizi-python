# Memorizzare una serie di numeri presi in input dall’utente, disordinati.
# Implementare l’algoritmo bubble sort per ordinarli in ordine crescente.

# chiedere lunghezza lista
while True:  # ciclo di controllo input
    try:
        lenLista = int(input("Quanti numeri vuoi inserire dentro le liste? "))  # chiedo la lungezza della lista
    except ValueError:  # eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

# compilo lista 1
lista = []  # creo una lista
for i in range(lenLista):  # ciclo for per inserire dentro la lista n valori decisi da utente
    while True:  # ciclo di controllo input
        try:
            num = float(input("Insersci un numero: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    lista.append(num)  # inserisco il numero dentro la lista

print("Lista:", lista)

