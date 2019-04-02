# from airport import Airport
# from terminal import Terminal
# from flight import Flight
# from aircraft import Aircraft
# from helicopter import Helicopter
# from plane import Plane
# from passenger import Passenger

# airport1.welcome_message()

print("1. Book a flight for a passenger")
print("2. See all passengers on a flight")
print("3. See all flights in a terminal")
print("4. Add aircraft to flight")
print("5. Change aircraft")
print("6. Cancel flight")

answer = input("What would you like to do?")

if answer == '1':
    print("Okay, proceed booking a flight now:")
    first_passenger_name = input("What is passenger name?")
    second_passenger_name = input("What is passenger surname?")
    passenger_age = input("What is the age of passenger?")


    if passenger_age < str(18):
        print("Passenger is not old enough to book a flight")
    else:
        print("Proceed. Which flight would you like?")

# get user input
# save to variables
# create a Passanger object

# list flights
# ask user which flight to book

# add Passanger object (append to flight list


elif answer == '2':
    print("All passengers in a flight: ")
    which_flight = input()

elif answer == '3':
    print("All flights in a terminal: ")
elif answer == '4':
    print("Add aircraft to flight: ")
elif answer == '5':
    print("Change aircraft: ")
elif answer == '6':
    print("Cancel fight: ")
else:
    print("Error: Invalid option!")


