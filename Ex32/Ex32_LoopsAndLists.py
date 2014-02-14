#List creation
hairs = ['brown',' blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits  = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This for-loop cylees throug elements of the List
for number in the_count:
	print "This is a count %d" % number

#Another for-loop that cycles through a List
for fruit in fruits:
	print "A fruit of a type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

#We can also build lists, first start with an empty cne
elements = []

# then we use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)

# now we can prin them out too
for i in elements:
	print "Element was: %d" %i




