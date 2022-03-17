listaNum = [] #creo una lista vuota dove inserire i numeri

while True: #ciclo infinito con dentro un break
    inputUtente = input("Inserisci un numero, oppure premi \"x\" per uscire: ") #prendo l'input dell'utente
    if inputUtente != "x" and inputUtente != "X": #controllo se l'utente vuole uscire o continuare
        listaNum.append(inputUtente) #inserisco l'input nella lista
    else:
        break

print(listaNum)

