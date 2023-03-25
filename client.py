import socket as soc
import threading as th
from adv import *

display()

c = soc.socket()
port = 4328
c.connect(('127.0.0.1', port))

# user = input("Enter your username: ")
# c.send(user.encode('ascii'))
user = "Ritabrata"

while True:
    print(f"Welcome {user}. What do you want to do today: \n")
    print("1. Car Booking\n2. Hotel Booking\n3. Flight Booking\n4. Exit\n")

    select = input("Select the operation (1-4): ")
    if (not select.isdigit()):
        print("\nWrong input. Please enter a number between 1 to 4. Try again.\n")
        continue

    if int(select) == 1:
        print("\nWe are operational in the following cities: ")
        display_car()
        print()
        src = input("Enter the name of the city from where you want to go: ")
        dest = input("Enter the destination where you want to go: ")
        choice = "car," + src.lower().strip() + "," + dest.lower().strip()

    elif int(select) == 2:
        print("\nWe are operational in the following cities and hotels: ")
        display_hotel()
        print()
        dest = input("Enter the name of the city where you want to book the hotel: ")
        hotel = input("Enter the name of the hotel: ")
        choice = "hotel," + dest.lower().strip() + "," + hotel.lower().strip()

    elif int(select) == 3:
        print("\nWe are operational in the following cities: ")
        display_flight()
        print()
        src = input("Enter the name of the city from where you want to go: ")
        dest = input("Enter the destination where you want to go: ")
        choice = "flight," + src.lower().strip() + "," + dest.lower().strip() 

    elif int(select) == 4:
        cnf = input("Are you sure you want to exit? Type \'Yes\' to confirm: ")
        if(cnf.lower() == "yes"):
            break 
        else:
            continue

    else:
        print("\nWrong choice. Please select again!!!\n")
        continue

    c.send(choice.encode('ascii'))

    ans = c.recv(1024).decode('ascii')
    print(f"\nResult: {ans}\n")

print(f"\nThank you {user} for using our services. Wishing you a great day ahead!!")
c.close()
