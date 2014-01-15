print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()


#raw_input
#If the prompt argument is present it is written to standard output without a trailing newline. 
#The function then reads a line from input, converts it to a stirng and returns that
#When EOF is read, EOFError is raised

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
