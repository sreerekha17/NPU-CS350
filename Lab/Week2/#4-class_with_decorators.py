###### Problem 4 ##########
# Given a Person class:
# class Person():	
#     def __init__(self, name):
#         self.name = name
        
#     def saying(self, stuff):
#         return stuff
        
#     def asking(self, stuff):
#         return self.saying("Would you please " + stuff)
    
#     def greeting(self):
#         return self.saying("Hello, my name is " + self.name)
# Complete this class to make it repeat the last thing said by adding a repeating method. Here's an example of its use:
# jim = Person("Jim Kelvin")
# jim.repeating()                  		 # starts at whatever value you want
# 'I am thinking about one of Python functions!'
# jim.saying("Hello")
# 'Hello'
# jim.repeating()
# 'Hello'
# jim.greeting()
# 'Hello, my name is Jim Kelvin'
# jim.repeating()
# 'Hello, my name is Jim Kelvin'
# jim.asking("register for the inoculation?")
# 'Would you please register for the inoculation?' 
# jim.repeating()
# 'Would you please register for the inoculation?' 

class Person():
    lastSaid = 'I am thinking about one of Python functions!'
    
    def __init__(self, name):
        self.name = name
    def storeLastSaid(method):
        def innerFunctionWrapper(*args):            
            Person.lastSaid = method(*args)
            return method(*args)
        return innerFunctionWrapper
    
    @storeLastSaid
    def saying(self, stuff):
        return stuff
    
    @storeLastSaid
    def asking(self, stuff):
        return self.saying("Would you please " + stuff)
    
    @storeLastSaid
    def greeting(self):
        return self.saying("Hello, my name is "+ self.name)
    
    @staticmethod
    def repeating():
        return Person.lastSaid

jim = Person("Jim Kelvin")
print(jim.repeating())      # starts at whatever value you want
                            #'I am thinking about one of Python functions!'
print(jim.saying("Hello"))  #'Hello'
print(jim.repeating())      #'Hello'
print(jim.greeting())       #'Hello, my name is Jim Kelvin'
print(jim.repeating())      #'Hello, my name is Jim Kelvin'
print(jim.asking("register for the inoculation?")) #'Would you please register for the inoculation?' 
print(jim.repeating())       #'Would you please register for the inoculation?' 
