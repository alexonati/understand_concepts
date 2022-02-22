operations = {
    "average": lambda seq: sum(seq) / len (seq),
    "total": sum,
    "top": max
    }

students = [
    {"name" : "Alex", "grades": (90, 89, 75, 45)},
    {"name" : "Maria", "grades": (70, 44, 99)}
]


for student in students:
        name = student ["name"]
        grades = student["grades"]

        print( f"Student : {name} ")
        operation = input("Enter 'average', 'total' or 'top': ")

        result = operations[operation](grades)
        print(result)
