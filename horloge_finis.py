from datetime import datetime
import time
import os
import keyboard

# ajoute les seconde, minutes et heure
def boucle(tuple):
    tuple = (tuple[0], tuple[1], tuple[2] + 1)
    if tuple[2] == 60:
        tuple = (tuple[0], tuple[1] + 1, 0)
    if tuple[1] == 60:  
        tuple = (tuple[0] + 1, 0, 0)
    if tuple[0] == 24:
        tuple = (0, 0, 0)
    return tuple
            
# affiche l'heure en fonction du mode selectionné
def afficher_heure(tuple, choix):
    os.system('cls')
    if choix == "1":
        heure = tuple[0] % 12 or 12
        suffix = "AM" if tuple[0] < 12 else "PM"
        print(f"{heure:02}:{tuple[1]:02}:{tuple[2]:02} {suffix}")
    elif choix == "2":
        print(f"{tuple[0]:02}:{tuple[1]:02}:{tuple[2]:02}")

# met pause au script
def pause():
    input("Entrée pour continuer...")

# verifie si l'heure est egal à l'alarme
def alarme(tuple, heure_alarme, minute_alarme, seconde_alarme):
    if tuple[0] == heure_alarme and tuple[1] == minute_alarme and tuple[2] == seconde_alarme :
        for _ in range(3):
            os.system('cls')
            time.sleep(0.5)
            print("Ceci sert d'alarme")
            time.sleep(1)

# demande de choisir entre le mode AM/PM ou 24h
def am():
    choix = input("""Affichage de l'heure:
1 - 12 heures AM/PM
2 - 24 heures
Faites votre choix : """)
    
    if choix == "1":
        return choix
    elif choix == "2":
        return choix
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        am()

# commence le script
tuple = (16, 30, 0)
mtn = datetime.now()
heure_alarme, minute_alarme, seconde_alarme = map(int, input("Entrez l'alarme (H M S) : ").split())
choix = am()

# boucle mere du script
while True:
    afficher_heure(tuple, choix)
    alarme(tuple, heure_alarme, minute_alarme, seconde_alarme)
    debut_temps = datetime.today().timestamp()
    while datetime.today().timestamp() - debut_temps < 1:
        if keyboard.is_pressed('backspace'):
            pause()
    
    tuple = boucle(tuple)