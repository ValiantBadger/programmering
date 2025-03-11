import random

class Passenger:
    def __init__(self, name: str, destination: int):
        self.name = name
        self.destination = destination


class Wagon:
    def __init__(self, passengers : list[Passenger]):
        self.passengers = passengers


class Train:
    def __init__(self, wagons : list[Wagon], line: int, position: int):
        self.wagons = wagons
        self.line = line
        self.position = position


class Station:
    def __init__(self, name: str, passengers : list[Passenger]):
        self.name = name
        self.passengers = passengers

class Line:
    def __init__(self, name: str, stops: list):
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
    Station("Goonhole", []),
    Station("Dilltown", []),
    Station("Lowtapertown", []),
    Station("Gigatown", [])
    ]

lines = [
    Line("Red", [0, 1, 2, 3, 4, 5]),
    Line("green", [6, 7, 8, 9, 10, 11]),
]


trains = [
    Train([Wagon([]), Wagon([]), Wagon([]), Wagon([])], 0, 0),
    Train([Wagon([]), Wagon([]), Wagon([]), Wagon([])], 1, 0),
]


passenger = ["Goonalisa", "Bob the rizzler", "Chadron", "Cringezilla", "Rizzus Maximus", "Goonericus", "Simp Slayer","tuah", "Sunshine King", "LeSunshine", "Solar LeBron", "Crazyfrog", "Gonga"]

for station in stations:
    if passenger:
        passenger_name = passenger.pop(0)
        station.passengers.append(Passenger(passenger_name, random.choice(range(len(stations)))))


def move_train(train: Train):
            train.position = (train.position + 1) % len(lines[train.line].stops)


def move_all_trains():
    for train in trains:
        move_train(train)


def unload_train(train: Train):
    current_station = lines[train.line].stops[train.position]
    for wagon in train.wagons:
        stations[current_station].passengers.extend([p for p in wagon.passengers if p.destination == current_station])
        wagon.passengers = [p for p in wagon.passengers if p.destination != current_station]

def unload_all_trains():
    for train in trains:
        unload_train(train)


def load_train(train: Train):
    current_station = lines[train.line].stops[train.position]
    for wagon in train.wagons:
        while stations[current_station].passengers:
            wagon.passengers.append(stations[current_station].passengers.pop(0))

def load_all_trains():
    for train in trains:
        load_train(train)


def print_state():
    for i, train in enumerate(trains):
        print(f"Train {i} on line {lines[train.line].name} at station {stations[lines[train.line].stops[train.position]].name}")
        for j, wagon in enumerate(train.wagons):
            print(f"Wagon {j} has passengers {[p.name for p in wagon.passengers]}")
    for i, station in enumerate(stations):
        print(f"Station {i} has passengers {[p.name for p in station.passengers]}")

def main():
    for _ in range(20):  
        print_state()
        input("Press enter to move trains")
        move_all_trains()
        unload_all_trains()
        load_all_trains()

if __name__ == "__main__":
    main()

