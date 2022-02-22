from random import choice

questions = ["Why is there a face on the moon?",
                     "Why is the sky blue?",
                     "Why do babies cry?",
                     "Where are all the dinosaurs?",
                    "Who was Einstein?"]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?").strip().lower()

print("Oh...ok...")

    
