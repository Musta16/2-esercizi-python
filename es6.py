# Memorizzare una serie di numeri presi in input dall’utente.
# Ordinarli in ordine crescente.
# Memorizzare un ulteriore numero preso in input dall’utente.
# Implementare l’algoritmo di ricerca dicotomica per mostrare se il numero sia presente o meno nella serie

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

# ordino la lista (crescente)
lista.sort()
print("Lista ordinata:", lista)

# chiedere un numero
while True:  # ciclo di controllo input
    try:
        n = int(input("Inserisci un numero da memorizzare: "))  # chiedo la lungezza della lista
    except ValueError:  # eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

# ricerca binaria
inf = 0  # inidice inferiore
sup = len(lista) - 1  # indice inferiore
trovato = False

while (inf <= sup) and (not trovato):  # ciclo finché inferiore e superiore non collidono
    medio = (inf + sup) // 2  # calcolo la posizione media tra i due
    if (lista[medio] < n):  # controllo se la posizione media corrisponde o meno all'indice di n
        inf = medio + 1
    elif (lista[medio] == n):
        trovato = True
    else:
        sup = medio - 1

if trovato:
    print("Il numero memorizzato", n, "è presenta nella lista in posizione", medio)
else:
    print("Il numero memorizzato", n, "NON è presenta nella lista")
