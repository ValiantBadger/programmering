import random

class Passenger:
    def __init__(self, name : str, destination : int):
        self.name = name
        self.destination = destination
 
class Wagon:
    def __init__(self, passengers : list[Passenger]):
        self.passengers = passengers
   
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
 
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)
        pass
 
 
class Train:
    def __init__(self, wagons : list[Wagon], line : int, position : int):
        self.wagons = wagons
        self.line = line
        self.position = position
   
class Station:
    def __init__(self, name : str, passengers : list[Passenger]):
        self.name = name
        self.passengers = passengers
   
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
   
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)
        pass
 
class Line:
    def __init__(self, name : str, stops : list[int]):
        self.name = name
        self.stops = stops

stations = [
    Station("Goontown", []),
    Station("Doonland", []),
    Station("Outland", []),
    Station("Casttin", []),
    Station("Doomtown", []),
    Station("Goonland", []),
    Station("GOONERLAND", []),
    Station("GoonerTown", []),
    Station("Hawk", []),
    Station("Goonhole", [])
    ]


lines = [
    Line("Red", [0, 3, 7, 8, 9]),
    Line("green", [1, 2, 4, 5, 6]),
]


trains = [
    Train([Wagon([]), Wagon([]), Wagon([]), Wagon([])], 0, 0),
    Train([Wagon([]), Wagon([]), Wagon([]), Wagon([])], 1, 0),
]

names = ["Goonalisa", "Bob the rizzler", "Chadron", "Cringezilla", "Rizzus Maximus", "Goonericus", "Simp Slayer","tuah", 
         "Sunshine King", "LeSunshine", "Solar LeBron", "Crazyfrog", "Gonga"]



for i in range(len(stations)):
    name = random.choice(names)
    destination = 0

    for line in lines:
        for stop in line.stops:
            if i == stop:
                destination = random.choice(line.stops)
    
    passenger = Passenger(name, destination)
    stations[i].passengers.append(passenger)

for station in stations :
    print(station.passengers[0].name, station.passengers[0].destination)

# game loop bitch ass

for i in range(20):
    for train in trains:
        station_position = lines[train.line].stops[train.position]
        station = stations[station_position]
        for passenger in station.passengers:
            if passenger.destination != station_position:
                station.remove_passenger(passenger)
                train.wagons[0].add_passenger(passenger)

    for train in trains:
        line = lines[train.line]
        if train.position < len(line.stops) -1:
            train.position += 1
        else:
            train.position = 0

    for i in range(len(stations)):
        for passenger in stations[i].passengers:
            print(f"Passageraren vill till {i} och hamnade på {passenger.destination}")