print "You enter a dark room with two doors. Do you go through door #1 or Door #2?"

door = raw_input("> ")

if door == '1':
	print "There is a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake"
	print "2. Scream at the bear."

	bear  = raw_input("> ")
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your leff off. Good job!"
	else: 
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into th enedless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacked chothespsins."
	print "3. Understanding revolvers yellow melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "You body survices power by a mind jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of much. Good Jobs"


else:
	print "You stubmle around and fall on a knife and die. Good job!"