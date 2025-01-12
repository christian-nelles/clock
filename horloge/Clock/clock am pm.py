from datetime import datetime

now = datetime.now()

formatted_time = now.strftime('%I:%M:%S %p')

user_choice = input("Affichage de l'heure: \n A - 12 heures \n B - 24 heures")
print(user_choice)

if user_choice == "A" :
    print (formatted_time)

elif user_choice == "B" :
    print (now)