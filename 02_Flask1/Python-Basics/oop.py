mylist = [1,2,3]

mylist.append(4)

print(type(mylist))
print(type(mylist) is list)

class Sample():
    pass 

z = Sample()

print(type(z))

class Dog():
    # Class Object Attributes: true for all the instances in the class
    species = 'mammal'

    def __init__(self, breed):
        self.breed = breed

x = Dog(breed='lab')
print(x.breed)
print(x.species)
Dog.species = 'fish'
x.species = 's'
print(x.species)
print(Dog.species)


class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * self.pi

myCircle = Circle(10)
print(myCircle.radius)
print(myCircle.area())

class Animal():
    def __init__(self, fur):
        self.fur = fur
        print('Animal Created!')

    def report(self):
        print('Animal')
    
    def eat(self):
        print('Eat')

a = Animal('fuzzy')
a.report()
a.eat()

class Dog(Animal):

    def __init__(self, fur):
        Animal.__init__(self, fur)
        print('Dog Created!')

    # Method overriding
    def report(self):
        print('Dog')

d = Dog('strange')
d.report()
d.eat()
print(d.fur)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.pages

mybook = Book("Python rocks!", 'Jose', 250)
print(mybook)
print(len(mybook))