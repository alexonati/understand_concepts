#the 1st digit in the dictionary values represents the age and the 2nd represents the number of seats available

films = {
    "Captain America": [7,65],
    "Avengers": [18,45],
    "Is this the end": [10,100],
    "Meet the Parents":[9, 66]
    }

while True:

    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age

        if age >= films[choice][0]:
            # check enough seats

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")
    
