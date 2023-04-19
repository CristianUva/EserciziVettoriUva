##3M Uva Cristian
#Esercizio 4
#max 4 voti per studente per N studenti

#file con cognomi studenti di una classe --> lista
#file con al massimo 4 voti per studente --> array
#leggere informazioni da file
#stampare la media dei voti per singolo alunno
#stampare la media dei voti degli studenti della classe
#quale tipo di dato usare?.

#Importo la libreria numpy per utilizzare gli array
import numpy as np

#Crea un array vuoto di dimensione 10
voti = np.zeros((10,4))
cognomi = []

#Leggi i voti dal file
file = "voti.txt"
with open(file) as file:
    i = 0
    for line in file:
        # Divide la riga in 4 voti
        voti_studente = line.rstrip().split(",") # Rimuove gli spazi inutili e le virgole e converte in float
        voti[i] = [float(v) for v in voti_studente]
        i += 1
        
#Leggo i cognomi        
file2 = "cognomi.txt"
with open(file2) as file2:
    i = 0
    for line in file2:
        cognome = float(line.strip()) # Rimuove gli spazi inutili e converte in float
        cognomi.append(cognome) # Aggiunge il voto alla lista

# Calcolo la media dei voti per ogni studente
media_studenti = np.mean(voti, 1)      #Uso la libreria per fare la media
#media_voti = np.sum(voti) / len(voti)  #Si può fare usando la libreria, o il ciclo for.
#Calcolo della media generale
somma_voti = 0
for voto in voti:
    somma_voti += voto    
media_voti = somma_voti / len(voti)

#Stampo i voti e la media
for i in range len(cognomi):
    print(f"Voti dello studente {cognomi[i]}:")
for voto in voti:
    print(voto)
print("\nMedia dei voti per studente:")
for media in media_studenti:
    print(media)
print("\nMedia dei voti della classe:", media_voti)