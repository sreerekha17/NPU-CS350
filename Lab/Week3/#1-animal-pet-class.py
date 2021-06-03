# Problem #1:
# Assuming two classes are given, so called Anml(i.e. Animal) and Pet as follows, 

# current_year = 2018

# class 	Anml(object): 
#     def __init__(self): 
#            	        self.is_alive = True 		# It’s alive!!!
 
# class 	Pet(Anml): 
# def __init__(self, name, year_of_birth, owner=None): 
#     Anml.__init__(self) 		# call the parent’s constructor 
#     self.name = name 
#     self.age = current_year - year_of_birth 
#     self.owner = owner 

#     def eating(self, thing): 
#          print(self.name + " ate a " + str(thing) + "!") 

#                             def talking(self): 
#                                  print("...")


# now complete two Cat & AnnoyingCat classes as children of class Pet, using parent methods wherever possible, and verify the correctness of your class in some objects. 

# class 	Cat(Pet): 
# def __init__(self, name, yob, owner, lives=5): 
# """ Initialize the class members """




# def 	talking(self): 
# """ While asked talking, a cat says ' Meow!' """ 



# def	lose_life(self): 
# """
# When a class member ' lives' reaches zero, the 'is_alive' variable becomes False
# """




# class	AnnoyingCat(Cat): 
#                             def __init__(self, name, yob, owner, lives=5): 
# """ Initialize the class members """


#  		    def talking(self): 
# """
# The AnnoyingCat, just like a Cat, will always repeat what he/she said twice.
# """



current_year = 2018

class Anml(object):
    def __init__(self):
        self.is_alive = True

class Pet(Anml):
    def __init__(self, name, year_of_birth, owner=None):
        Anml.__init__(self)
        self.name = name
        self.age = current_year - year_of_birth
        self.owner = owner
    
    def eating(self, thing):
        print(self.name + " ate a " + str(thing) + '!' )
    
    def talking(self):
        print("...")

class Cat(Pet):
    def __init__(self, name, yob, owner, lives=5): # Initialize class members"""
            Pet.__init__(self, name, yob, owner)
            self.lives = lives
    def talking(self): # Cat says Meow
        print("Meow!")
    
    def lose_life(self):      # when a class member life becomes 0,  is_alive variable becomes False
        self.lives -= 1
        if (self.lives == 0):
            self.is_alive = False 

class AnnoyingCat(Cat):
    _repeatsTalk = 2
    def __init__(self, name, yob, owner, lives=5): #initialize class members"
        Cat.__init__(self, name, yob, owner, lives)
    
    def talking(self): # The annoying cat just like a cat will always repeat what he/she said twice"
        for i in (0, AnnoyingCat._repeatsTalk):
            Cat.talking(self)


# creates a charlie - as annoying cat born in 2016
charlie = AnnoyingCat('Charlie', 2016, 'Mike', 6)
print(charlie.name)
print(charlie.owner)
charlie.talking()
print("charlie's age is", charlie.age)
charlie.eating('fish')

#creates oreo, a normal cat instance 
oreo = Cat("Oreo", 2017, "Leo", 4)
print(oreo.name)
print(oreo.owner)
oreo.talking()
print("Oreo's is", oreo.age, " year old")

#creates another cat with name Fluffy who is 11 years old, and has only one yer left
fluffy = Cat("Fluffy", 2007, 'Lucy', 1)
fluffy.lose_life()
print("Fluffy alive", fluffy.is_alive)

#creates a new child class Bunny from Pet
class Bunny(Pet):
    def __init__(self, name, yob, owner, breed, lives = 7):
        Pet.__init__(self, name, yob, owner)
        self.breed = breed
        self.lives = lives
    
    def eating(self, thing):
        self.favorite = thing
        Pet.eating(self, thing)


snowball = Bunny('Snowball', 2014, 'Charles', 'European Rabbit', 9)

thunder = Bunny('Thunder', 2017, 'Charles', 'Lionhead', 1)

print("Snowball is ", snowball.age, "years old")
print("Thunder is", thunder.age, "year old" )


