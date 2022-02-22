import random

health = 50

#difficulty easy mode is 1, medium mode is 2 and hard mode is 3

difficulty = 2

potion_health =  int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health) 
 
