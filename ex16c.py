# To use the argv command to take the filename as the argument.
from sys import argv

# Taking filename as a parameter passed to the python script.
script, filename = argv

# To check with user if they want to overwrite the file mentioned.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Wait to let the user hit CTRL-C if they do not wish to overwrite.
raw_input("?")

# To open the file mentioned by the filename.
print "Opening the file..."
target = open(filename, 'w')

# Truncating the file by deleting all its contents.
print "Truncating the file. Goodbye!"
target.truncate()

# Asking user to input the three lines that will go into the file.
print "Now I'm going to ask you for three lines."

# Getting the lines from the user one by one.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Writing the lines into the file followed by the return.
print "I'm going to write these to the file."

input = "%r \n %r \n %r \n" % (
	line1, line2, line3)

target.write(input)

# Closing the file after the writing job is done.
print "And finally, we close it."
target.close()