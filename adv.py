import string    
import random  
import json
  
def display():
    banner = """

        ████████╗██████╗░██╗██████╗░░░░░░░░█████╗░██████╗░██╗░░░██╗██╗░██████╗░█████╗░██████╗░
        ╚══██╔══╝██╔══██╗██║██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║██║██╔════╝██╔══██╗██╔══██╗
        ░░░██║░░░██████╔╝██║██████╔╝█████╗███████║██║░░██║╚██╗░██╔╝██║╚█████╗░██║░░██║██████╔╝
        ░░░██║░░░██╔══██╗██║██╔═══╝░╚════╝██╔══██║██║░░██║░╚████╔╝░██║░╚═══██╗██║░░██║██╔══██╗
        ░░░██║░░░██║░░██║██║██║░░░░░░░░░░░██║░░██║██████╔╝░░╚██╔╝░░██║██████╔╝╚█████╔╝██║░░██║
        ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

        ------------------------------ MADE BY TEAM SOCKET404 --------------------------------
        """
    print(banner)

def display_car():
    with open('car.json', 'r') as f:
        car_city = json.load(f)
    print("{:<10} {:<20}".format('CITY', 'AVAILABLE CARS'))
 
    for key, value in car_city.items():
        print("{:<10} {:<20}".format(key, str(value)))

def display_hotel():
    with open('hotel.json', 'r') as f:
        hotel_city = json.load(f)
    print("{:<10} {:<20} {:<10}".format('CITY', 'HOTEL', 'NUMBER OF ROOMS'))
 
    for key, value in hotel_city.items():
        for i in value:
            name, num = i            
            print("{:<10} {:<20} {:<10}".format(key, name, num))

def display_flight():
    with open('flight.json', 'r') as f:
        flights = json.load(f)
    print("{:<15} {:<13} {:<13} {:<10}".format('AIRLINE', 'FROM', 'TO', 'AVAILABLE TICKETS'))
    
    for key, value in flights.items():
        for i in value:
            src, dest, num = i
            print("{:<15} {:<13} {:<13} {:<10}".format(key, src, dest, num))

def verifyCar(c):
    with open('car.json', 'r') as f:
        car_city = json.load(f)
    return c.capitalize() in car_city

def checkCarAvailability(c):
    with open('car.json', 'r') as f:
        car_city = json.load(f)
    return car_city[c.capitalize()]
      
def genTicket():
    return str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))

def verifyHotelCity(city):
    with open('hotel.json', 'r') as f:
        hotel_city = json.load(f)
    return city in hotel_city

def verifyHotelMatch(city, hotel):
    with open('hotel.json', 'r') as f:
        hotel_city = json.load(f)
    for i in hotel_city[city]:
        if i[0] == hotel:
            return True
    return False

def verifyHotelAvailability(city, hotel):
    with open('hotel.json', 'r') as f:
        hotel_city = json.load(f)
    for i in hotel_city[city]:
        if i[0] == hotel:
            ans = i[1]
            break
    return ans 

def genRoomNumber():
    return random.randint(100, 300)

def existPath(src, dest):
    with open('flight.json', 'r') as f:
        flights = json.load(f)
    for key, val in flights.items():
        for i in val:
            fr, to, num = i
            if(src == fr and to == dest):
                return key
    return ""

def checkSeatAvailability(airline, src, dest):
    with open('flight.json', 'r') as f:
        flights = json.load(f)
    for val in flights[airline]:
            fr, to, num = val
            if(src == fr and to == dest):
                return num 
    return 0

def genSeatNumber():
    return random.randint(100, 500)