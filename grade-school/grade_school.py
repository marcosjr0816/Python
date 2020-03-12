class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students:
            self.students[grade].append(name)
        else:
            self.students.update({grade:[name]})

    def roster(self):
        stu = []
        for i in sorted(self.students):
            self.students[i].sort()
            stu = stu + self.students[i]
        return stu

    def grade(self, grade_number):
        if grade_number not in self.students:
            return []
        else:
            self.students[grade_number].sort()
            return self.students[grade_number]
