class Passenger:
    def __init__(self, first_name, last_name, age):
        self.passenger_first_name = first_name
        self.passenger_last_name = last_name
        self.age = age
        self.flight = ""


    def add_flight(self, flight):
        self.flight = flight
