class Flight:
    def __init__(self, flight_number, aircraft = "", destination, terminal, date, cancelled = False ):
        self.flight_number = flight_number
        self.aircraft = aircraft
        self.destination = destination
        self.terminal = terminal
        self.passengers = []
        self.date = date
        self.cancelled = cancelled

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def add_or_change_aircraft(self, aircraft):
        self.aircraft = aircraft

    def cancel_flight(self):
        self.cancelled = True
