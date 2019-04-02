from airport import Airport
from terminal import Terminal
from flight import Flight
from passenger import Passenger
from aircraft import Aircraft
from helicopter import Helicopter
from plane import Plane

airport1 = Airport("Heathrow", "London")

terminal1 = Terminal(1, "T1")
terminal2 = Terminal(2, "T2")

flight1 = Flight("1", "India", "01/05/2019")
flight2 = Flight("2", "California", "20/07/2019")
flight3 = Flight("3", "St. Lucia", "23/10/2019")
flight4 = Flight("4", "Paris", "11/11/2019")
flight5 = Flight("5", "Australia", "05/10/2019", True)

passenger1 = Passenger("Reagan", "Prince", 22)
passenger2 = Passenger("Eimantas", "Alejunas", 25)
passenger3 = Passenger("Mariam", "Aslam", 25)
passenger4 = Passenger("Laura", "Geanta", 28)
passenger5 = Passenger("Alun", "Wrighton", 28)
passenger6 = Passenger("Iman", "Ali", 24)

helicopter1 = Helicopter("H001")
plane1 = Plane("P001")
plane2 = Plane("P002")

flight1.add_passenger(passenger1)
flight1.add_passenger(passenger2)
flight2.add_passenger(passenger3)
flight2.add_passenger(passenger4)
flight3.add_passenger(passenger5)
flight3.add_passenger(passenger6)

flight1.select_aircraft(plane1)
flight2.select_aircraft(plane1)
flight3.select_aircraft(plane2)
flight4.select_aircraft(plane2)

terminal1.add_airport(airport1)
terminal2.add_airport(airport1)

flight1.add_terminal(terminal1)
flight2.add_terminal(terminal2)
flight3.add_terminal(terminal1)
flight4.add_terminal(terminal2)


passenger1.add_flight(flight1)
passenger2.add_flight(flight1)
passenger3.add_flight(flight2)
passenger4.add_flight(flight2)
passenger5.add_flight(flight3)
passenger6.add_flight(flight3)

terminal1.add_flight(flight1)
terminal2.add_flight(flight2)
terminal1.add_flight(flight3)
terminal2.add_flight(flight4)


plane1.add_flight(flight1)
plane1.add_flight(flight2)
plane2.add_flight(flight3)
plane2.add_flight(flight4)

airport1.add_terminal(terminal1)
airport1.add_terminal(terminal2)

airport1.see_flights()
