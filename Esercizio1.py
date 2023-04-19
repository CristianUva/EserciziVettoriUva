#3M Uva Cristian
#Esercizio 1
#1. file con un voto per studente per 10 studenti con una riga per ogni voto leggere informazioni da file stampare
#la media dei voti degli studenti della classe quale tipo di dato usare?

#Importo la libreria numpy per utilizzare gli array
import numpy as np

#Crea un array vuoto di dimensione 10
voti = np.zeros(10)

#Leggi i voti dal file
file = "voti.txt"
with open(file) as file:
    i = 0
    for line in file:
        voti[i] = float(line.rstrip()) #Serve a togliere gli spazi inutili
        i += 1
        
#Calcolo la media dei voti
#media_voti = np.sum(voti) / len(voti)  #Si può fare usando la libreria, o il ciclo for.
somma_voti = 0
for voto in voti:
    somma_voti += voto
#Calcolo della media
media_voti = somma_voti / len(voti)

#Stampo i voti e la media
print("Voti degli studenti:")
for voto in voti:
    print(voto, end=" ")
print("\nMedia dei voti:", media_voti)
