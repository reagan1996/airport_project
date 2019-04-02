class Flight:
    def __init__(self, flight_number, destination, date, cancelled = False):
        self.flight_number = flight_number
        self.destination = destination
        self.terminal = None
        self.passengers = []
        self.date = date
        self.cancelled = cancelled

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def select_aircraft(self, aircraft):
        self.aircraft = aircraft

    def add_terminal(self,terminal):
        self.terminal = terminal

    def cancel_flight(self):
        self.cancelled = True

