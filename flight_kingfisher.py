import socket as soc
import json
from aux_func import *

while True:
    s =  soc.socket()
    print("Socket successfully created")

    port = 4002
    s.bind(('127.0.0.1', port))
    print(f"Socket successfully binded to port: {port}")

    s.listen(5)
    print("Waiting for connection...\n")

    c, addr = s.accept()

    while True:
        reply = ""
        with open('./data/flight.json', 'r') as f:
            flights = json.load(f)
        reply += "{:<13} {:<13} {:<10}\n".format( 'FROM', 'TO', 'AVAILABLE TICKETS')
    
        for key, value in flights.items():
            if key == "KingFisher":
                for i in value:
                    src, dest, num = i
                    reply += "{:<13} {:<13} {:<10}\n".format(src, dest, num)

        c.send(str(reply).encode('ascii'))
                
        data = c.recv(1024).decode('ascii')

        if(not data):
            break
        
        print(f"Data Received: {data}\n")
        src, dest, user = data.split(',')
        src = src.capitalize()
        dest = dest.capitalize()
        airline="KingFisher"
        check = existPath(src, dest, airline)
        if(check == ""):
            reply = "Sorry. We cannot provide any airline. Try again."
        elif not checkSeatAvailability(src, dest, airline):
            reply = "Sorry. We don't have any available seats. Please wait."
        else:
            with open('./data/flight.json', 'r') as f:
                flights = json.load(f)
            for i in flights[airline]:
                if i[0] == src and i[1] == dest:
                    i[2] = i[2] - 1
                    break
            with open("./data/flight.json", "w") as f:
                json.dump(flights, f, indent=4)
            reply = f"Your flight has been booked at {airline} airlines from {src} to {dest} for \'{user}\'. Seat No.: {genSeatNumber()}"

        print(f"Result: {reply}\n")
        c.send(str(reply).encode('ascii'))
    c.close()




    
