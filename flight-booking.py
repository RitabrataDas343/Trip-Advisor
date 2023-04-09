import socket as soc
from aux_func import *

while True:
    flight_socket =  soc.socket()
    print("Socket successfully created")

    port = 4000
    flight_socket.bind(('127.0.0.1', port))
    print(f"Socket successfully binded to port: {port}")

    flight_socket.listen(5)
    print("Waiting for connection...\n")

    c, addr = flight_socket.accept()

    while True:
        data = c.recv(1024).decode('ascii')

        if(not data):
            break
        
        print(f"Data Received: {data}\n")
        airline, user = data.split(',')

        if(int(airline) == 1):
            spicejet_socket = soc.socket()
            spicejet_socket.connect(('127.0.0.1', 4001))
            welcome = "Welcome to SpiceJet airlines"
            c.send(str(welcome).encode('ascii'))
            menu = spicejet_socket.recv(1024).decode('ascii')
            c.send(str(menu).encode('ascii'))
            param = c.recv(1024).decode('ascii')
            print(f"Result: {param}\n")
            spicejet_socket.send(param.encode('ascii'))
            reply = spicejet_socket.recv(1024).decode('ascii')
            c.send(str(reply).encode('ascii'))
            spicejet_socket.close()
        elif(int(airline) == 2):
            kingfisher_socket = soc.socket()
            kingfisher_socket.connect(('127.0.0.1', 4002))
            welcome = "Welcome to KingFisher airlines"
            c.send(str(welcome).encode('ascii'))
            menu = kingfisher_socket.recv(1024).decode('ascii')
            c.send(str(menu).encode('ascii'))
            param = c.recv(1024).decode('ascii')
            print(f"Result: {param}\n")
            kingfisher_socket.send(param.encode('ascii'))
            reply = kingfisher_socket.recv(1024).decode('ascii')
            c.send(str(reply).encode('ascii'))
            kingfisher_socket.close()
        elif(int(airline) == 3):
            indigo_socket = soc.socket()
            indigo_socket.connect(('127.0.0.1', 4003))
            welcome = "Welcome to Indigo airlines"
            c.send(str(welcome).encode('ascii'))
            menu = indigo_socket.recv(1024).decode('ascii')
            c.send(str(menu).encode('ascii'))
            param = c.recv(1024).decode('ascii')
            print(f"Result: {param}\n")
            indigo_socket.send(param.encode('ascii'))
            reply = indigo_socket.recv(1024).decode('ascii')
            c.send(str(reply).encode('ascii'))
            indigo_socket.close()
    c.close()




    
