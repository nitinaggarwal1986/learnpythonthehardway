# From the module sys importing the argv to take parameters from user.
from sys import argv

# Taking filenamen from the user via argv.
script, filename = argv

# To open text file with location given by filename and store the file 
# in the variable txt to be called later.
txt = open(filename)

# Printing the filename followed by the content of the file.
print "Here's your file %r:" % filename
print txt.read()

# Asking for another filename from the user.
print "Type the filename again:"
file_again = raw_input("> ")

# To open the file and store it into variable txt_again.
txt_again = open(file_again)

# To print the content of the second file by using the function read on 
# the file txt_again.
print txt_again.read()