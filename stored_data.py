from airport import Airport
from terminal import Terminal
from flight import Flight
from passenger import Passenger
from aircraft import Aircraft
from helicopter import Helicopter
from plane import Plane

airport1 = Airport("Heathrow", "London")

terminal1 = Terminal(1, "T1")
terminal1.add_airport(airport1)

terminal2 = Terminal(2, "T2")
terminal2.add_airport(airport1)

flight1 = Flight("1", "India", "01/05/2019")
flight1.add_terminal(terminal1)

flight2 = Flight("2", "California", "20/07/2019")
flight2.add_terminal(terminal1)

flight3 = Flight("3", "St. Lucia", "23/10/2019")
flight3.add_terminal(terminal2)

flight4 = Flight("4", "Paris", "11/11/2019")
flight4.add_terminal(terminal2)

flight5 = Flight("5", "Australia", "05/10/2019", True)

helicopter1 = Helicopter("H101",)

plane1 = Plane("P001")
plane1.add_flight(flight1)
plane1.add_flight(flight3)

plane2 = Plane("P002")
plane2.add_flight(flight2)
plane2.add_flight(flight4)




