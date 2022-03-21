# memorizzare una serie di parole prese in input da utente
# memorizzare un numero preso da input utente
# costruire una nuova serie con solamente le parole più lunghe del numero
# soluzioni: 1. liste SENZA comprehension - 2. liste CON comprehension

lenLista = int(input("Quanti parole vuoi inserire dentro alla lista? ")) #chiedo la lungezza della lista
listaString = [] #creo una lista per parole
for i in range(lenLista): #ciclo for per inserire dentro la lista n valori decisi da utente
    parola_String = input("Insersci una parola: ")
    listaString.append(parola_String)

numConfronto = int(input("Inserisci un numero da memorizare: ")) # memorizzo un numero

listaParoleLunghe = [] #creo una lista per le parole lunghe più di n
for e in listaString: # ciclo per controllare la lunghezza delle parole
    if len(e) > numConfronto:
        listaParoleLunghe.append(e)

print("Ecco la lista di parole di lunghezza maggiori di",numConfronto, ": ", listaParoleLunghe)