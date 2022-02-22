#ask user for name

name = input("What is your name? ")

#ask user for age

age  = input("How old are you? ")

#ask user where they live - city

city = input("What city do you live in? ")

#ask user what they enjoy

love = input("What do you like doing? ")

#create output text

text_to_print = "Your name is {} and you are {} years old and you live in {} and you love {}."
output = text_to_print.format(name, age, city, love)

#print user input

print(output)
