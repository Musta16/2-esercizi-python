# Memorizzare una serie di numeri con duplicati presi in input dall'utente
# Mostrare solo i numeri univoci della serie: 1. usando solo le liste - 2. usando solo i set

# 1. usando solo le liste

lenLista = int(input("Quanti numeri vuoi inserire dentro alla lista? ")) #chiedo la lungezza della lista
l = [] #creo una lista
for i in range(lenLista): #ciclo for per inserire dentro la lista n valori decisi da utente
    num_String = input("Insersci un numero: ")
    num = float(num_String) #converto la stringa di numeri in float
    l.append(num)