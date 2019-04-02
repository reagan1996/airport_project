class Airport:
    def __init__(self, name, location):
        self.airport_name = name
        self.terminal = []
        self.airport_location = location

    def add_terminal(self, terminals):
        self.terminal.append(terminals)

    def welcome_message(self):
        print("Welcome to ", self.airport_name, " Airport." )




airport1 = Airport("Gatwick", "East")

airport1.add_terminal("g1")

# airport1 = Airport("Gatwick", "East")
# airport1.add_terminal("g1")
# print(airport1.terminal[0])

