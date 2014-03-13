## Animal is-a object (yes, sort of confusing look at the xtra credit
class Animal(object):
	pass

## Dog is a class 
class Dog(Animal):

	def __init__(self, name):
		# Dog has-a name
		self.name = name

## Cat is a class of type Animal
class Cat(Animal):

	def __init__(self, name):
		#Cat has-a name
		self.name = name

# Person is-a object 
class Person(object):

	def __init__(self, name):
		#Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None


# Employee is a class of type Person
class Employee(Person):

	def __init__(self, name, salary):
		# how you can run the __init__ method of a parent class reliably. Go search for "python super" and read the various advice on it being evil and good for you.
		super(Employee,self).__init__(name)
		#Empoyee has-a salary
		self.salary = salary

# Fish is-a object 
class Fish(object):
	pass

# Salmon is-a class of type Fish
class Salmon(Fish):
	pass

# Halibut is-a class of type fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

# Mary is-a person
mary = Person("Mary")

# Mary has-a pet satan
mary.pet = satan

#Frank is-a employee
frank = Employee("Frank",120000)

#Frank has-a pet rover
frank.pet = rover

#Flipper is-a fish
flipper = Fish()

#crouse is-a salmon
crouse = Salmon()

#Harry is-a Halibut
harry = Halibut()







