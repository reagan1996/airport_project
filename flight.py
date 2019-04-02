class Flight:
    def __init__(self, flight_number, destination, date, cancelled = False, aircraft = "" ):
        self.flight_number = flight_number
        self.aircraft = aircraft
        self.destination = destination
        self.terminal = ""
        self.passengers = []
        self.date = date
        self.cancelled = cancelled

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def add_or_change_aircraft(self, aircraft):
        self.aircraft = aircraft

    def cancel_flight(self):
        self.cancelled = True

    def add_terminal(self,terminal):
        self.terminal = terminal
        terminal.flights.append(self)
