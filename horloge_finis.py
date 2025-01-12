from datetime import datetime
import time
import os
import keyboard

def boucle(t):
    t = (t[0], t[1], t[2] + 1)
    if t[2] == 60:
        t = (t[0], t[1] + 1, 0)
    if t[1] == 60:  
        t = (t[0] + 1, 0, 0)
    if t[0] == 24:
        t = (0, 0, 0)
    return t
            
def afficher_heure(t, user_choice):
    os.system('cls')
    if user_choice == "1":
        hour = t[0] % 12 or 12
        suffix = "AM" if t[0] < 12 else "PM"
        print(f"{hour:02}:{t[1]:02}:{t[2]:02} {suffix}")
    elif user_choice == "2":
        print(f"{t[0]:02}:{t[1]:02}:{t[2]:02}")

def pause():
    input()

def alarme(t, h, m, s):
    if t[0] == h and t[1] == m and t[2] == s :
        for _ in range(3):
            os.system('cls')
            time.sleep(0.5)
            print("it's time to wake up")
            time.sleep(1)

def am():
    user_choice = input("""Affichage de l'heure:
1 - 12 heures AM/PM
2 - 24 heures
Faites votre choix : """)
    
    if user_choice == "1":
        return user_choice
    elif user_choice == "2":
        return user_choice
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        am()


t = (16, 30, 0)
now = datetime.now()
formatted_time = now.strftime('%I:%M:%S %p')
h, m, s = map(int, input("Entrez l'alarme (H M S) : ").split())
user_choice = am()

while True:
    afficher_heure(t, user_choice)
    alarme(t, h, m, s)
    start_time = datetime.today().timestamp()
    while datetime.today().timestamp() - start_time < 1:
        if keyboard.is_pressed('backspace'):
            pause()
    
    t = boucle(t)