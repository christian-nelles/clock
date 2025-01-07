import time
import os
import keyboard

def init():
    global t
    t = (0, 0, 0) 

def boucle():
    global t
    t = (t[0], t[1], t[2] + 1)
    if t[2] == 60:
        t = (t[0], t[1] + 1, 0)
    if t[1] == 60:  
        t = (t[0] + 1, 0, 0)
    if t[0] == 24:
        init()
            
def afficher_heure():
        os.system('cls')
        print(f"{t[0]:02}:{t[1]:02}:{t[2]:02}")

def pause():
        input()
        time.sleep(0.1)

init()
while True:
    afficher_heure()
    start_time = time.time()
    while time.time() - start_time < 1.5:
        if keyboard.is_pressed('space'):
            pause()
    
    boucle()