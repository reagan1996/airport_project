class Airport:
    def __init__(self, name, location):
        self.airport_name = name
        self.terminals = []
        self.airport_location = location

    def add_terminal(self, terminal):
        self.terminals.append(terminal)

    def welcome_message(self):
        print("Welcome to ", self.airport_name, " Airport." )

    def see_flights(self):
        index = 1
        for terminal in self.terminals:
            for flight in terminal.flights:
                if not flight.cancelled:
                    print(str(index),". flight number:", flight.flight_number, ", destination: ", flight.destination, ", flight date: ", flight.date)
                    index = index + 1




# airport1 = Airport("Gatwick", "East")
# #
# # airport1.add_terminal("g1")

# airport1 = Airport("Gatwick", "East")
# airport1.add_terminal("g1")
# print(airport1.terminal[0])

