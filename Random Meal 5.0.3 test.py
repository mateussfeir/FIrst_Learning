from random import choice
import time

breakfast_protein_options = ['Egg (13% protein)', 'Sausage (14% protein)', 'Tofu (8~14% protein)', 'Chicken (27% protein)']
breakfast_carbohydrate_options = ['Bread (43% carbo)', 'Pasta(32.5% carbo)', 'Banana (23% carbo)', 'Sweet Potato (20% carbo)', "Potato (15% carbo)", "Rice (28% carbo)", "Oat (66% carbo)"]

lunch_protein_options = ['Chicken (27% protein)', 'Pork (25.7% protein)', 'Sushi (13% protein)', 'Salmon (21% protein)', "Beef (22% protein)", "Egg (13% protein)"]
lunch_carbohydrate_options = ['Bread (43% carbo', 'Pasta (43% carbo)', 'Banana (27% carbo)', 'Sweet Potato (20% carbo)', "Potato (15% carbo)", "Rice (42% carbo)", "Oat (66% carbo)"]

dinner_protein_options = ['Chicken (27% protein)', 'Pork (25.7% protein)', 'Sushi (13% protein)', 'Salmon (21% protein)', 'Tuna (30% protein)', "Beef (22% protein)", "Egg (13% protein)"]
dinner_carbohydrate_options = ['Korean noodle (66% carbo)', 'Bread (43% carbo', 'Salad (3% carbo)', 'Sweet Potato (20% carbo)', 'Oat (66% carbo)','Pasta (43% carbo)']

def meals():
    
    kind_of_meal = input("\nAre you going to have breakfast (br), lunch (l) or dinner (d)?\n ").lower()

    if kind_of_meal == "br" or kind_of_meal == "breakfast":
        time.sleep(0.25)
        answer = input("Do you rather based protein (p) or carbohydrate (c) or both (b)?\n").lower()       
        if answer == "p":
            time.sleep(0.25)
            print("Have a wonderful day, today your protein based food is: " + choice(breakfast_protein_options) + "!")
            time.sleep(0.5)
            answer2 = input("\nDo you wanna run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            elif answer2 == "n":
                print("\nOk, have a nice day.")
            else:
                time.sleep(0.25)
                print("\nSorry, we could not understand you, can you fill the infs again: ")
                time.sleep(0.25)
                meals()

        elif answer == "c":
            time.sleep(0.25)
            print("Today your carbohydrate based food is: " + choice(breakfast_carbohydrate_options) + "!")
            time.sleep(0.25)
            answer2 = input("\nDo you wanna run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            elif answer2 == "n":
                print("\nOk, have a nice day.")
            else:
                time.sleep(0.25)
                print("\nSorry, we could not understand you, can you fill the infs again: ")
                time.sleep(0.25)
                meals()

        elif answer =="b":
            time.sleep(0.25)
            print("Today your meal based in protein and carbohydrates is: " + choice(breakfast_protein_options) + " and " + choice(breakfast_carbohydrate_options) +"!")
            time.sleep(0.25)
            answer2 = input("Do you want to run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            elif answer2 == "n":
                print("\nOk, have a nice day.")
            else:
                time.sleep(0.25)
                print("\nSorry, we could not understand you, can you fill the infs again: ")
                time.sleep(0.25)
                meals()

        else: 
            time.sleep(0.25)
            print ("\nSorry, you are fucking stupid and u cant understand anything, try again: ")
            time.sleep(0.25)
            meals()

    elif kind_of_meal == "l" or kind_of_meal == "lunch":
        time.sleep(0.25)
        answer = input("Do you rather based protein (p) or carbohydrate (c) or both(b)?\n").lower()       
        if answer == "p":
            time.sleep(0.25)
            print("Have a wonderful lunch, today your protein based food is: " + choice(lunch_protein_options) + "!")
            time.sleep(0.25)
            answer2 = input("Do you want to run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            elif answer2 == "n":
                print("\nOk, have a nice day.")
            else:
                time.sleep(0.25)
                print("\nSorry, we could not understand you, can you fill the infs again: ")
                time.sleep(0.25)
                meals()

        elif answer == "c":
            time.sleep(0.25)
            print("Today your carbohydrate based food is: " + choice(lunch_carbohydrate_options) + "!")
            time.sleep(0.25)
            answer2 = input("\nDo you wanna run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            elif answer2 == "n":
                print("\nOk, have a nice day.")
            else:
                time.sleep(0.25)
                print("\nSorry, we could not understand you, can you fill the infs again: ")
                time.sleep(0.25)
                meals()
                
        elif answer =="b":
            time.sleep(0.25)
            print("Today your meal based in protein and carbohydrates is: " + choice(lunch_protein_options) + " and " + choice(lunch_carbohydrate_options) +"!")
            time.sleep(0.25)
            answer2 = input("Do you want to run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            elif answer2 == "n":
                print("\nOk, have a nice day.")
            else:
                time.sleep(0.25)
                print("\nSorry, we could not understand you, can you fill the infs again: ")
                time.sleep(0.25)
                meals()

        else: 
            time.sleep(0.25)
            print ("\nSorry, you are fucking stupid and u cant understand anything, try again: ")
            time.sleep(0.25)
            meals()


    elif kind_of_meal == "d" or kind_of_meal == "dinner":
        time.sleep(0.25)
        answer = input("Do you rather based protein (p) or carbohydrate (c) or both (b)?\n").lower()     
        if answer == "p":
            time.sleep(0.25)
            print("Have a wonderful Dinner, today your protein based food is: " + choice(lunch_protein_options) + "!")
            time.sleep(0.25)
            answer2 = input("\nDo you wanna run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            elif answer2 == "n":
                print("\nOk, have a nice day.")
            else:
                time.sleep(0.25)
                print("\nSorry, we could not understand you, can you fill the infs again: ")
                time.sleep(0.25)
                meals()

        elif answer == "c":
            time.sleep(0.25)
            print("Today your carbohydrate based food is: " + choice(lunch_carbohydrate_options) + "!")
            time.sleep(0.25)
            answer2 = input("\nDo you wanna run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            else:
                print("\nOk, have a nice day.")
        elif answer == "b":
            time.sleep(0.25)
            print("Today your meal based in protein and carbohydrates is: " + choice(lunch_protein_options) + " and " + choice(lunch_carbohydrate_options) +"!")
            time.sleep(0.25)
            answer2 = input("Do you want to run the program again? (y/n) ").lower()
            time.sleep(0.25)
            if answer2 == "y":
                meals()
            elif answer2 == "n":
                print("\nOk, have a nice day.")
            else:
                time.sleep(0.25)
                print("\nSorry, we could not understand you, can you fill the infs again: ")
                time.sleep(0.25)
                meals()

        else:
            time.sleep(0.25)
            print ("\nSorry, you are fucking stupid and u cant understand anything, try again: ")
            time.sleep(0.25)
            meals()

    else: 
            time.sleep(0.25)
            print ("\nSorry, you are fucking stupid and u cant understand anything, try again: ")
            time.sleep(0.25)
            meals()

meals()