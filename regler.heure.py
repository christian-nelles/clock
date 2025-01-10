from datetime import datetime
import time
import os
import keyboard

def boucle():
    global t
    t = (t[0], t[1], t[2] + 1)
    if t[2] == 60:
        t = (t[0], t[1] + 1, 0)
    if t[1] == 60:  
        t = (t[0] + 1, 0, 0)
    if t[0] == 24:
        t = (0, 0, 0)
            
def afficher_heure():
    os.system('cls')
    print(f"{t[0]:02}:{t[1]:02}:{t[2]:02}")

def pause():
    input()

def alarme():
    alarm = (0, 0, 10)
    if t[0] == h and t[1] == m and t[2] == s :
        print ("it's time to wake up")
        
        for i in range(3):
            os.system('cls')
            time.sleep(0.5)
            print("it's time to wake up")
            time.sleep(1)

i = 0
t = (16, 30, 0) 

h, m, s = map(int, input("Entrez l'heure (HH:MM:SS) : ").split())

while True:
    afficher_heure()
    alarme()
    start_time = datetime.today().timestamp()
    while datetime.today().timestamp() - start_time < 1.5:
        if keyboard.is_pressed('backspace'):
            pause()
    
    boucle()
    
  