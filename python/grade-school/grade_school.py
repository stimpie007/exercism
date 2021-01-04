class School:
    def __init__(self):
        self.grades = {i: [] for i in range(1, 8)}

    def add_student(self, name, grade):
        self.grades[grade].append(name)

    def roster(self):
        return [name for grade in self.grades.values() for name in sorted(grade)]

    def grade(self, grade_number):
        return sorted(self.grades[grade_number])
