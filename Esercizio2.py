#3M Uva Cristian
#2. file con un voto per studente per n studenti con una riga per ogni voto leggere informazioni da file stampare
#la media dei voti degli studenti della classe quale tipo di dato usare?

#Importo la libreria numpy per utilizzare gli array

#Crea una lista vuota di dimensione da destinarsi
voti = []

#Leggi i voti dal file
file = "voti.txt"
with open(file) as file:
    i = 0
    for line in file:
        voto = float(line.strip()) # Rimuove gli spazi inutili e converte in float
        voti.append(voto) # Aggiunge il voto alla lista
        
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