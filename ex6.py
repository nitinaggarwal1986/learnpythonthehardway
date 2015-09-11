# Here we define a few string type variables. We put x as a sting
# which takes a string inside it, and y does it twice.
x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Print x and y.
print x
print y

# Print two strings with x and y contained in them.
print "I said: %r." % x
print "I also said: '%s'." % y

# Here we define two variables. 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# We print a combination of above two variables. Notice %r in thae
# variable joke_evaluation.
print joke_evaluation % hilarious

# Again we define two variables w and e as strings.
w = "This is the left side of..."
e = "a string with a right side."

# We print the addition of above two variables. As we are printing
# two variables we will get a concatinated string returned to us.
print w + e