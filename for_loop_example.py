for number in range(1,987,7):
    print(number)


for letter in "abcdefghijklmnopqrstuvwxyz":
    print(letter)

vowels = 0
consonants = 0

word = input("Please enter your word in order to count the vowels/consonants: ").lower()


for letter in word:
    if letter in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels.".format(vowels))
print("There are {} consonants.".format(consonants))

students = {
    "male": ["Emily", "Ana", "Valentina"],
    "female" : ["Ioan","Marc","Dan","Tim","Tom" ]
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
