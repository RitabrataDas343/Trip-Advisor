import socket as soc
import threading as th
from aux_func import *

def handle_client(conn, addr):
    username = conn.recv(1024).decode('ascii')
    username.strip()
    print(f"Client \'{username}\' has logged-in.\n")
    while True:
        data = conn.recv(1024).decode('ascii')
        info = list()
        
        if(not data):
            print(f"Client \'{username}\' has disconnected.\n")
            break 
        else:
            info = data.split(',')
            operations = info[0]
            print(f"Choice Received for \'{username}\': {operations.capitalize()} Booking.\n")

        if(operations == "car"):
            car_socket = soc.socket()
            car_socket.connect(('127.0.0.1', 2000))
            car_socket.send(str(info[1]+','+info[2]+','+username).encode('ascii'))
            result = car_socket.recv(1024).decode('ascii')
            print(f"Result: {result}\n")
            conn.send(str(result).encode('ascii'))
            car_socket.close()

        elif(operations == "hotel"):
            hotel_socket = soc.socket()
            hotel_socket.connect(('127.0.0.1', 6000))
            hotel_socket.send(str(info[1]+','+info[2]+','+username).encode('ascii'))
            result = hotel_socket.recv(1024).decode('ascii')
            print(f"Result: {result}\n")
            conn.send(str(result).encode('ascii'))
            hotel_socket.close()

        elif (operations == "flight"):
            flight_socket = soc.socket()
            flight_socket.connect(('127.0.0.1', 4000))
            flight_socket.send(str(info[1]+','+username).encode('ascii'))
            welcome = flight_socket.recv(1024).decode('ascii')
            print(f"Result for \'{username}\': {welcome}\n")
            conn.send(str(welcome).encode('ascii'))
            menu = flight_socket.recv(1024).decode('ascii')
            print(f"Result for \'{username}\':\n {menu}\n")
            conn.send(str(menu).encode('ascii'))
            param = conn.recv(1024).decode('ascii')
            print(f"Result for \'{username}\': {param}\n")
            flight_socket.send(str(param+','+username).encode('ascii'))
            reply = flight_socket.recv(1024).decode('ascii')
            conn.send(str(reply).encode('ascii'))
            print(f"Result for \'{username}\': {reply}\n")
            flight_socket.close()

        else:
            result = ""
            conn.send(str(result).encode('ascii'))

    conn.close()

display()
print("THIS IS THE ADMIN PANEL. ALL LOGS CAN BE FOUND HERE.\n")
print("Welcome Admin. You can view the logs below.\nLOGS:\n")

client_socket =  soc.socket()
port = 4328
client_socket.bind(('127.0.0.1', port))
client_socket.listen(5)

while True:
    conn, addr = client_socket.accept()
    t = th.Thread(target = handle_client, args=(conn, addr))
    t.start()
