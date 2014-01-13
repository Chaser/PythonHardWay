
# ~~~~~~~~ ESCAPE Characters
# 		\\			Backslash
#		\'			Single Quote
#		\"			Doub;le Quote
# 		\a			ASCII Bell (BEL)
#		\b 			ASCII Backspace (BS)
#		\f  		ASCII formfeed (FF)
#		\n 			ASCII linefeed (LF)
#		\N{name}	Character named name in the unicode database (Unicode only)
# 		\r 			ASCII Carriage Return (CR)
#		\t 			ASCII Horizontal Tabe (TAB)
# 		\uxxxx		Character with 16-bit hex value xxxx (Unicode only)
#		\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
#		\v  		ASCII Vertical Tabe (VT)
#		\ooo		Character with octal value ooo
#	  	\xhh		Character with hex value hh

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat ="I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print "%s" % fat_cat
print "%r" % fat_cat

#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" %i
