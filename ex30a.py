people = 30
cars = 40
trucks = 15

# if-elif-else statements to print lines for the cases when 
# cars > people, cars < people, and otherwise.
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else: 
	print "We can't decide."

# if-elif-else statements to print lines for the cases when 
# trucks > cars, trucks < cars, and otherwise.
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

# if-else statements to print lines for the cases when 
# people > trucks and otherwise.
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."