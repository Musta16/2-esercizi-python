# Memorizzare una serie di numeri presi in input dall’utente.
# Mostrare se la serie contiene numeri duplicati o meno.
# Mostrare quali sono i numeri duplicati, e quante volte sono ripetuti

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
    while True:  # ciclo di controllo input
        try:
            num = float(input("Insersci un numero: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    l1.append(num)  # inserisco il numero dentro la lista

for i in l1:
    dupli = l1.count(i)
    if dupli > 1:
        print("Dentro la lista il numero", i, "è duplicato", dupli, "volte!")

