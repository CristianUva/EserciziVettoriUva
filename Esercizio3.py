#3M Uva Cristian
#Esercizio 3
#4 voti per studente per 10 studenti
#
#file con 4 voti per studente per 10 studenti
#6.5,7,8.5,4
#5,6,3.5,6
#...
#leggere informazioni da file
#stampare la media dei voti per singolo alunno
#stampare la media dei voti degli studenti della classe
#quale tipo di dato usare?

#Importo la libreria numpy per utilizzare gli array
import numpy as np

#Crea un array vuoto di dimensione 10
voti = np.zeros((10,4))

#Leggi i voti dal file
file = "voti.txt"
with open(file) as file:
    i = 0
    for line in file:
        # Divide la riga in 4 voti
        voti_studente = line.rstrip().split(",") # Rimuove gli spazi inutili e le virgole e converte in float
        voti[i] = [float(v) for v in voti_studente]
        i += 1

# Calcolo la media dei voti per ogni studente
media_studenti = np.mean(voti, 1)       #Uso la libreria per fare la media
        
#media_voti = np.sum(voti) / len(voti)  #Si può fare usando la libreria, o il ciclo for.
#Calcolo della media generale
somma_voti = 0
for voto in voti:
    somma_voti += voto    
media_voti = somma_voti / len(voti)

#Stampo i voti e la media
print("Voti degli studenti:")
for voto in voti:
    print(voto)
print("\nMedia dei voti per studente:")
for media in media_studenti:
    print(media)
print("\nMedia dei voti della classe:", media_voti)