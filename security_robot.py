known_users = ["Alex", "Ioan", "Valentina"]

while True:

    print("Hi my name is SecuRoboto")
    name = input("What's your name? ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?").lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem. Have a nice day!")
    else:
        print("Hello {}. I don't think I've met you yet.".format(name))
        add_me = input("Would you like to be added to the system (y/n)?").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No problem. See you around.")
            
         

        
