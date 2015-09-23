# import the argv to call arguments at the script call from sys module.
from sys import argv

# Asking user to pass the file name as an argument.
script, input_file = argv

# To define a function to print the whole file passed into function as 
# a parameter f.
def print_all(f):
	print f.read()

# To define a rewind function to bring the current location on file back to
# starting position.
def rewind(f):
	f.seek(0)

# To define a function that will print the line at the position given bytearray
# line_count in the file f.
def print_a_line(line_count, f):
	print line_count, f.readline()

# To open the input_file in the variable name current_file.
current_file = open(input_file)

print "First let's print the whole file: \n"

# To print the whole of the file using print_all function.
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# To rewind the file to the original location so that it can be read from the
# start again.
rewind(current_file)

print "Let's print three lines:"

# To print the first three lines of the file by a consecutive calls of 
# print_a_line function.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)