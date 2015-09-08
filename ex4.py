# Defined cars as a variable with value 100.
cars = 100
# Defined space_in_a_car as a variable with value 4.0.
space_in_a_car = 4.0
# Defined drivers as a variable with value 30.
drivers = 30
# Defined passengers as a variable with value 90.
passengers = 90
# Defined cars_not_driven as a variable with its value as difference of 
# cars and drivers.
cars_not_driven = cars - drivers
# Defined cars_driven as a variable with value equal to drivers.
cars_driven = drivers
# Defined carpool_capacity as the product of cars_driven times the space_in_a_car.
carpool_capacity = cars_driven * space_in_a_car
# Defined the average_passengers_per_car as the ratio of passengers to cars_driven.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."