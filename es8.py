# Memorizzare una serie di numeri con duplicati presi in input dall'utente
# Mostrare solo i numeri univoci della serie: 1. usando solo le liste - 2. usando solo i set

# chiedo lunghezza lista
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
    while True:  # ciclo di controllo input
        try:
            num = float(input("Insersci un numero: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    l1.append(num)  # inserisco il numero dentro la lista

# 1. usando solo le liste

listaUnica = []
for i in l1:
    if i not in listaUnica:
        listaUnica.append(i)

print("Lista numeri univoci:", listaUnica)

# 2. usando solo i set

print("Set numeri univoci:", set(l1))
