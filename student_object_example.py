class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Alex Ion', [9, 8, 7, 6, 9])
student_two = Student('Maria Nae', [10, 10, 9, 10])

print(student_one.__class__)
print(student_one.average())
print(student_two.average())
