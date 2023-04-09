import socket as soc
import json
from aux_func import *

while True:
    s =  soc.socket()
    print("Socket successfully created")

    port = 6000
    s.bind(('127.0.0.1', port))
    print(f"Socket successfully binded to port: {port}")

    s.listen(5)
    print("Waiting for connection...\n")

    c, addr = s.accept()

    while True:
        data = c.recv(1024).decode('ascii')

        if(not data):
            break
        
        print(f"Data Received: {data}\n")
        dest, hotel = data.split(',')
        dest = dest.capitalize()
        if(len(hotel.split()) != 2):
            reply = "Hotel name not appropriate. Should contain 2 words."
        else:
            start, end = hotel.split(' ')
            hotel = start.capitalize() + ' ' + end.capitalize()
            if(not verifyHotelCity(dest)):
                reply = "Sorry. We are not operational in the above city. Try again."
            elif(not verifyHotelMatch(dest, hotel)):
                reply = "The given hotel is not in the mentioned city. Try again."
            elif not verifyHotelAvailability(dest, hotel):
                reply = "Sorry. We don't have any available rooms. Please wait."
            else:
                with open('./data/hotel.json', 'r') as f:
                    hotel_city = json.load(f)
                for i in hotel_city[dest]:
                    if i[0] == hotel:
                        i[1] = i[1] - 1
                        break
                with open("./data/hotel.json", "w") as f:
                    json.dump(hotel_city, f, indent=4)
                reply = f"Your hotel has been booked at {hotel}, {dest}. Room No.: {genRoomNumber()}"

        print(f"Result: {reply}\n")
        c.send(str(reply).encode('ascii'))
    c.close()




    
