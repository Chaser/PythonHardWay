#Symbol AND
if (True and True):
	print "Statement is true"

# Symbol del
# deletes an item from a list
friends = ["Chase", "Ty", "Helen", "Jazzie", "Sas", "Hayls", "Heidi"]
print friends 
#Delete an item
del friends[6]
print friends

#all can delete multiple items
del friends [4:6]
print friends

# Symbole from
# Does not introduce the module name from which imports are taken from in the local symbol table 

# Symbol NOT
if not(False):
	print "Statment is also true"

# Symbol is while
eval = True
while (eval == True):
	print "Evaluation is true"
	eval = false

print "Evaluation is false"

# Symbol as 
as


# Symbol elif
if (True == False):
	print "In the if statement" 
elif (True == True)
	print "In the else if statement"
else:
	print "In the else statement"

# Symbol global
my_age = 24

def Set_Age():
	#When modifying a global variable require the global statement
	global my_age 
	my_age = 24 

def Display_Age():
	# Do not require the global statement for reading, only modification
	print my_age 


# Symbol or
if (True or True)
	print "The or is true if it can be seen"

# Symbol with
with 


# Symbol assert
assert 


#Symbol else
else:

#Symbol if
if (True):
	print "The if evaluation is true"

#Symbol pass
pass

#Symbol yield
yield

#Symbol break
break

#Symbol except
except

#Symbol import
import 

#Symbol print
print "Testing print yeaa har"

#Symbol class
class

#Symbol exec
exec

#Symbol in
in 

#Symbol raise
raise 

#Symbol continue
continue

#Symbol finally
finally

#Symbol is
is

#Symbol return
return

#Symbol def
def

#Symbol for
for

#Symbol lambda
lamda

#Symbole try


#******************** Data types
booleanLogic1 = True
print type(booleanLogic1)

booleanLogic2 = False
print type(booleanLogic2)

# Frequenctly used  to represent the absence of a value, as when default arguments are not passed to a function. Assignments to None are illegal and raise a syntaxError
noType = None
print type(NoType)


stringExample = "Hello Chase"
print type(stringExample)

floatExample = 32.00
print type(floatExample)

listExample = [1,2,3,4,5,6]
print type(listExample)


#******************** String Escape Sequences
\\
\'
\"
\a
\b
\f
\n
\r
\t
\v

#******************** String Formats
%d
%i
%o
%u
%x
%X
%e
%E
%f
%F
%g
%G
%c
%r
%s
%%


#******************** Operators

-
*
**
/
//
%
<
>
<=
>=
==
!=
<>
( )
[ ]
{ }
@
,
:
.
=
;
+=
-=
*=
/=
//=
%=
**=