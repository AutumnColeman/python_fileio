from sys import argv # Lines 1 - 3 get a filename

script, filename = argv

txt = open(filename) #opens the file...obviously

print "Here's your file %r:" % filename
print txt.read() #reads the file without parameters

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
