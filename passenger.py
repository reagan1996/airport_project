class Passenger:


    def __init__(self, first_name, last_name, flight, age):
        self.passenger_first_name = first_name
        self.passenger_last_name = last_name
        self.flight = flight
        self.age = age


    def add_to_flight(self, flight):
        self.flight = flight
        flight.add_passenger.append(self)
