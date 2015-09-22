# Create a function cheese_and_cracker to mention things about the
# amount of cheese and crackers mentioned by the arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# Instance where you pass the arguments to the function directly.
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# Instance where you define variables and pass the variables as the
# arguments to the function.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Instance where you pass the result of math operation + to the function.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Instance where you pass the result of math operation combined on variables
# and numbers to the function as arguments. 
print "And we can combine the two, variable and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)