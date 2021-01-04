class Garden:
    PLANTS = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }
    STUDENTS = [
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry"
    ]

    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram.rsplit()
        self.students = sorted(students)

    def plants(self, student_name):
        student_index = self.students.index(student_name)
        student_plants = list()

        for row in range(2):
            student_plants.append(self.diagram[row][student_index * 2])
            student_plants.append(self.diagram[row][student_index * 2 + 1])

        return [self.PLANTS[plant] for plant in student_plants]
