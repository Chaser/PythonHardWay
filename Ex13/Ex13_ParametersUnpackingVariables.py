#import of modules/libraries
from sys import argv

#argv is "argument variable". Holds the arguments you pass to your Python script
#when you run it
script, first, second, third = argv
#Command line arguments are always strings!!!

print "The script is called", script
print "Your first variable is:", first 
print "Your second variable is:", second
print "Your third variable is:", third

