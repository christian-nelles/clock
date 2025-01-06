import time
import os

def init():
    global t
    t = (0, 0, 0) 

def boucle():
    global t
    while True:
        os.system('cls')
        print(f"{t[0]:02}:{t[1]:02}:{t[2]:02}")
        time.sleep(1)
        t = (t[0], t[1], t[2] + 1)
        if t[2] == 60:
            t = (t[0], t[1] + 1, 0)
        if t[1] == 60:
            t = (t[0] + 1, 0, 0)
        if t[0] == 24:
            init()
            
init()
boucle()