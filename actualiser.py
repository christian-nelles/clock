from datetime import datetime
import time
import os 

def boucle():
  os.system('cls')
  print(datetime.now().strftime("%H,%M,%S"))
  time.sleep(1)
  boucle()

boucle()


# while True:
#   boucle()   (deuxieme façon si j'enlève la boucle d'au-dessus)