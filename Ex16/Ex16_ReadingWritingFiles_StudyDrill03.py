#import of modules/libraries
from sys import argv

#argv is "argument variable". Holds the arguments you pass to your Python script
#when you run it
script, filename = argv
#Command line arguments are always strings!!!

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Trucating the file. Goodbye!"
target.truncate()			#Empties the file. w+ does not require this step!

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it"
target.close()

print "Checking file write..."
readfile = open(filename,'r')

print 'Displaying File Contents'
print readfile.read();
