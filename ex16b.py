from sys import argv

script, filename = argv

txt = open(filename)

print "Reading the file %r." % filename
print txt.read()
