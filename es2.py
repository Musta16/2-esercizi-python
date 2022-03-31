# Memorizzare una serie di numeri presi in input dall’utente.
# Mostrarne media e deviazione standard (import math, math.sqrt() per radice quadrata)
import math

while True:  # ciclo di controllo input
    try:
        lenLista = int(input("Quanti numeri vuoi inserire dentro alla lista? "))  # chiedo la lungezza della lista
    except ValueError:  # eccezione
        print("Non hai inserito un numero! Ritenta!")
        continue
    else:
        break

l = []  # creo una lista

for i in range(lenLista):  # ciclo for per inserire dentro la lista n valori decisi da utente
    while True:  # ciclo di controllo input
        try:
            num = float(input("Insersci un numero: "))
        except ValueError:  # eccezione
            print("Non hai inserito un numero! Ritenta!")
            continue
        else:
            break

    l.append(num)  # inserisco il numero dentro la lista

somma = 0  # imposto la somma a zero
for i in range(len(l)):  # ciclo per sommare tutti i numeri dentro la lista
    somma += l[i]  # sommo "somma" al numero corrispondende all'indice

media = somma / lenLista
devStandFalsa = math.sqrt(somma / lenLista)

print("La media è: ", media)
print("La deviazine standard(falsa) è: ", devStandFalsa)
print("Lista: ", l)
print("Lungezza lista: ", len(l))  # printo lunghezza lista
