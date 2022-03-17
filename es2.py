import math

lenLista = int(input("Quanti numeri vuoi inserire dentro alla lista? ")) #chiedo la lungezza della lista
l = [] #creo una lista
for i in range(lenLista): #ciclo for per inserire dentro la lista n valori decisi da utente
    num_String = input("Insersci un numero: ")
    num = float(num_String) #converto la stringa di numeri in float
    l.append(num)

somma = 0 #imposto la somma a zero
for i in range(len(l)): #ciclo per sommare tutti i numeri dentro la lista
    somma += l[i] #sommo "somma" al numero corrispondende all'indice

media = somma/lenLista
devStandFalsa = math.sqrt(somma / lenLista)

print("La media è: ", media)
print("La deviazine standard(falsa) è: ", devStandFalsa)
print("Lista: ", l)
print("Lungezza lista: ", len(l)) #printo lunghezza lista