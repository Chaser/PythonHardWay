ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in taht list, lets fix that."

#Breaks down the string into a list
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]				#Prints last item out
print stuff.pop()			#Gets last item
print ' '.join(stuff)		#Joins all items together
print '#'.join(stuff[3:5])  #Joins items 3 & 4 together

