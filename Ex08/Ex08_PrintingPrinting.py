#Should only use %r for getting debugging information about something. The %r will give you the "representation"
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")			#Output will be single quotes as python prints strings the most efficient way possible !
print formatter % (True,False,False,True)				#Key words so do not neet quotes 
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"I had this thing.",								#Output will be single quotes as python prints strings the most efficient way possible !
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
