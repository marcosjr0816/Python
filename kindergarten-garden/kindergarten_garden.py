class Garden:
    def __init__(self, diagram, students=[]):
        self.students = sorted(students)
        self.diagram = list(diagram.replace("\n", ""))
        self.plant = {
            'R': 'Radishes',
            'C': 'Clover',
            'G': 'Grass',
            'V': 'Violets'
        }

    def plants(self, student):
        result = []
        if student in self.students:
            for letter in self.diagram:
                if letter in self.plant:
                    result.append(self.plant[letter])
                    print(result)
            return result
        else:
            for letter in self.diagram:
                if letter in self.plant:
                    result.append(self.plant[letter])
                    print(result)
            return result
