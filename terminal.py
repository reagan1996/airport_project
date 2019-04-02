class Terminal:

    def __init__(self, id, name, airport):
        self.terminal_id = id
        self.terminal_name = name
        self.flights = []
        self.airport = airport

    def add_flights(self, flight):
        self.flights.append(flight)


terminal1 = Terminal("id1", "T1", "Gatwick")   # airport1
terminal1.add_flights("BNY656") # flight1
print(terminal1.flights)


'this is a change'