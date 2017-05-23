class Animal(object):
			"""docstring for Student"""
			def run(self):
				print("Animal is running....")
						
class Dog(Animal):
	def run(self):
		print("Dog is running...")
	def eat(self):
		print("Eating meat...")
class Cat(Animal):
	def run(self):
		print("Cat is running...")
	def eat(self):
		print("Eating fish...")
class Tortoise(Animal):
	"""docstring for Tortoise"""
	def run(self):
		print("Tortoise is running slow...")
class Timer(Animal):
	"""docstring for Timer"""
	def run(self):
		print("Start...")
def run_twice(animal):
	animal.run()
	animal.run()		
		
dog = Dog()
cat = Cat()
print(dog.run())
print(cat.run())
run_twice(Animal())	
run_twice(Timer())	