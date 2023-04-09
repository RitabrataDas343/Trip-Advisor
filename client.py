import socket as soc
from aux_func import *

display()

server_socket = soc.socket()
port = 4328
server_socket.connect(('127.0.0.1', port))

user = input("Enter your username: ")
server_socket.send(user.encode('ascii'))

while True:
    print(f"Welcome \'{user}\'. What do you want to do today: \n")
    print("1. Car Booking\n2. Hotel Booking\n3. Flight Booking\n4. Exit\n")

    select = input("Select the operation (1-4): ")
    if (not select.isdigit()):
        print("\nWrong input. Please enter a number between 1 to 4. Try again.\n")
        continue

    if int(select) == 1:
        print("\nWe are operational in the following cities: ")
        display_car()
        print()
        source = input("Enter the name of the city from where you want to go: ")
        destination = input("Enter the destination where you want to go: ")
        choice = "car," + source.lower().strip() + "," + destination.lower().strip()

    elif int(select) == 2:
        print("\nWe are operational in the following cities and hotels: ")
        display_hotel()
        print()
        destination = input("Enter the name of the city where you want to book the hotel: ")
        hotel = input("Enter the name of the hotel: ")
        choice = "hotel," + destination.lower().strip() + "," + hotel.lower().strip()

    elif int(select) == 3:
        print("\nWe have the following airlines available: ")
        display_flight()
        print()
        choice_num = input("Enter the number of the airline you want to pursue: ")
        if (not choice_num.isdigit()):
            print("\nWrong input. Please enter a number. Try again.\n")
            continue
        if(int(choice_num) in range(1,4)):
            choice_num = "flight," + choice_num
        else:
            print("\nWrong choice. Please select again!!!\n")
            continue
        server_socket.send(choice_num.encode('ascii'))
        welcome = server_socket.recv(1024).decode('ascii')
        print(f"\n{welcome}\n")
        menu = server_socket.recv(1024).decode('ascii')
        print(f"\n{menu}\n")

        source = input("Enter the name of the city from where you want to go: ")
        destination = input("Enter the destination where you want to go: ")
        choice = source.lower().strip() + "," + destination.lower().strip() 

    elif int(select) == 4:
        confirmation = input("Are you sure you want to exit? Type \'Yes\' to confirm: ")
        if(confirmation.lower() == "yes"):
            break 
        else:
            continue

    else:
        print("\nWrong choice. Please select again!!!\n")
        continue

    server_socket.send(choice.encode('ascii'))

    answer = server_socket.recv(1024).decode('ascii')
    print(f"\nResult: {answer}\n")

print(f"\nThank you \'{user}\' for using our services. Wishing you a great day ahead!!")
server_socket.close()
