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
