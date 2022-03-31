#Memorizzare una serie di numeri presi in input dall’utente. Mostrare la serie in ordine di inserimento e in ordine inverso

listaNum = [] #creo una lista vuota dove inserire i numeri
while True: #ciclo di controllo input
    try:
        dimensioneLista = int(input("Quanti numeri vuoi inserire? "))
    except ValueError: #eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

for i in range(dimensioneLista): #ciclo infinito con dentro un break
    while True: #ciclo di controllo input
        try:
            inputUtente = int(input("Inserisci un numero: ")) #prendo l'input dell'utente
        except ValueError: #eccezzione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break
    listaNum.append(inputUtente) #inserisco il numero dentro la lista
print(listaNum)

