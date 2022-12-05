import time
class human_Infs:
    
    # Defining informations of the object (human being's mind) using __init__ and then self. 

    def __init__(self, name, age, cars_Preference):
        self.name = name
        self.age = age
        self.cars_Preference = cars_Preference

    # Defining the function to run the code using the variables and strings without having to rewrite in every sentence

    def my_func(self):
        print("His name is " + self.name + ",", "he is " + self.age + " years old", "and he loves " +self.cars_Preference)

# Filling the objects with the informations

mind1 = human_Infs("Mateus", "28", "Tesla")
mind2 = human_Infs("Joacas", "23", "Volks")
mind3 = human_Infs("Gorilla Monster", "Undefinded", "Volwo")

# Calling the variables and the functions

Answer = input("You can bring one personality to the light, there are 3 personalities defined until now, but problably we will discover more, by the way, choose one personality (1/2/3) ")

if Answer == "1":
    time.sleep(0.25)
    mind1.my_func()
elif Answer == "2":
    time.sleep(0.25)
    mind2.my_func()
elif Answer == "3":
    time.sleep(0.25)
    mind3.my_func()
