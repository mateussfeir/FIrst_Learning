# Creating a class called organism, here we are going to use the alive variable as True, cause of the organisms are alive.

class organism:
    alive = True

# The class calle animal is going to Inherite all of the atributes of the "Mother Class"

class animal(organism):

# So the Animal class already have the atribute "alive" and we can add a function making him able to eat for example:

    def eat(self):
        print("The animal is eating")

# Now lets create an animal called dog, and give him all of the animal atributes.

dog = animal()

# We can try to make the dog eat for example

dog.eat()

# And we can double check if the dog is alive

print (dog.alive)

    