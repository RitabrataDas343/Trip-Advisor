import socket as soc
import json
from adv import *

while True:
    s =  soc.socket()
    print("Socket successfully created")

    port = 4000
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
        src, dest = data.split(',')
        src = src.capitalize()
        dest = dest.capitalize()
        airline = existPath(src, dest)
        if(airline == ""):
            reply = "Sorry. We cannot provide any airline. Try again."
        elif not checkSeatAvailability(airline, src, dest):
            reply = "Sorry. We don't have any available seats. Please wait."
        else:
            with open('flight.json', 'r') as f:
                flights = json.load(f)
            for i in flights[airline]:
                if i[0] == src and i[1] == dest:
                    i[2] = i[2] - 1
                    break
            with open("flight.json", "w") as f:
                json.dump(flights, f)
            reply = f"Your flight has been booked at {airline} airlines from {src} to {dest}. Seat No.: {genSeatNumber()}"

        print(f"Result: {reply}\n")
        c.send(str(reply).encode('ascii'))
    c.close()




    
