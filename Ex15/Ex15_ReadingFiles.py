#import of modules/libraries
from sys import argv

#argv is "argument variable". Holds the arguments you pass to your Python script
#when you run it
script, filename = argv
#Command line arguments are always strings!!!

txt = open(filename)							#Creates a file handle

print "Here's you file %r:" % filename			#Displays filename
print txt.read()								#Prints out file content to console

print "Type the filename again:" 
file_again = raw_input("> ")					#Asks for filename again

txt_again = open(file_again)					#Opens new file handle

print txt_again.read()							#Prints content of new file handle to console

