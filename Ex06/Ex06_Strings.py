x = "There are %d types of people." % 10						#x variable with a decimal display of 10
binary = "binary"												#Binary variable is of type string
do_not = "don't"												#do_not variable is of type string
y = "Those who know %s and those who %s." % (binary,do_not)     #y variable with binary and do_not variable

print x 														
print y												

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

