# Getting the name of the file from the user
print "Type the filename:"
file_name = raw_input("> ")

# To open the file with name stored as string in file_name.
txt = open(file_name)

# Printing the content of the file txt using read function.
print txt.read()