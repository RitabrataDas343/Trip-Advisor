import socket as soc
from aux_func import *

while True:
    s =  soc.socket()
    print("Socket successfully created")

    port = 2000
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
        if(not verifyCar(src)) or (not verifyCar(dest)):
            reply = "Sorry. We are not operational in the above city. Try again."
        elif not checkCarAvailability(src):
            reply = "Sorry. We don't have any available cars. Please wait."
        else:
            src = src.capitalize()
            dest = dest.capitalize()
            with open('./data/car.json', 'r') as f:
                car_city = json.load(f)
            car_city[src] = car_city[src] - 1
            car_city[dest] = car_city[dest] + 1
            with open("./data/car.json", "w") as f:
                json.dump(car_city, f, indent=4)
            reply = f"Your car has been booked from {src} to {dest}. Ticket ID: {genTicket()}"

        print(f"Result: {reply}\n")
        c.send(str(reply).encode('ascii'))
    c.close()




    
