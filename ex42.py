## Animal is-a object (yes, sort of confusing) look at extra credit
class Animal(object):
    pass


## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name and has-a pet
        self.name = name
        ##Person has-a pet of some kind
        self.pet = None


## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee has-a name.
        #hmm what is this strange magic?
        #super calls the parent class-type and uses the function from the parent. Particularly useful when there are overlapping function names as a normal call would call within-class
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

class Super_Employee(Person):
    def __init__(self, name, jobs, salary, deets):
        super().__init__(name)
        self.jobs = jobs
        self.salary = salary
        self.details = deets

bob = Super_Employee("Bob", ['Scientist','Journalist','Student'], 30000, {"City":"San Francisco", "Neighborhood":"Inner Sunset", "Work":"Hospital", "Hobby":"Python"})
print(bob.details["City"], "\n", bob.details["Neighborhood"], "\n", bob.details["Hobby"])
print(bob.jobs[0], ' and ', bob.jobs[-2])


## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet (Satan)
mary.pet = satan
print(mary.pet.name)

## frank is-a Employee that has-a name (Frank) and has-a salary (120000)
frank = Employee("Frank", 120000)
print(frank.salary)

## frank has-a pet (rover)
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon that is-a Fish
crouse = Salmon()

## harry is-a Halibut that is-a Fish
harry = Halibut()
