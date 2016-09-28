#Write a program which when given the name of a file as a command line argument, will print the number of lines there are in the file.
from sys import argv

script, filename = argv

count = 0

 #used xreadlines method to count lines
for line in open(filename).xreadlines( ): count += 1

print "The input file is %d lines long" % count
