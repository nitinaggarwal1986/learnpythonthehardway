def getnum(num):
	num = num + 1
	return num
	
print "First way is to print it directly using a number, say 1."
print "getnum(1) = ", getnum(1)

print "Second is to use the function into itself."
print "getnum(getnum(1)) = ", getnum(getnum(1))


print "We can also take an input as a variable saved earlier."

var = 1

print "Say, var = ", var
print "And the function becomes getnum(var)= ", getnum(var)

print "Yet another way is to take a number from user and then use it."
print "Please enter a number:",
var1 = int(raw_input())

print "So, with var = ", var
print "getnum(var) = ", getnum(var)

print "We can add two numbers and pass these as an input."
print "getnum(1 + 2) = ", getnum(1 + 2)

print "We can add a number and a variable and pass it as an input."
print "getnum(var + 2) = ", getnum(var + 2)

print "We can take an input from the user,"
print "Enter a number:", 
var1 = int(raw_input())

print "And, we can add a number to it and pass it to a function:"
print "getnum(var1 + 3) = ", getnum(var1 + 3)

print "Or, we can add a variable to it and pass it to a function:"
print "getnum(var1 + var) = ", getnum(var1 + var)

print "We can also pass the result of the function output for this input to the function"
print "getnum(getnum(var1)) = ", getnum(getnum(var1))

print "Why don't we pass sum of an output with a variable or a number to the function?"
print "getnum(getnum(var1)+2) = ", getnum(getnum(var1)+2)
print "getnum(getnum(var1)+var) = ", getnum(getnum(var1)+var)
