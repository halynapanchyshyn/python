class Group():
    def __init__(self):
        self.students = []

    def add(self, student):
        try:
            if len(self.students) >= 10:
                raise ValueError("Max quantity reached!")
            else:
                self.students.append(student)
        except ValueError as err:
            print(err)

    def delete(self, student):
        self.students.remove(student)

    def search(self, student_surname):
        for student in self.students:
            if student.surname == student_surname:
                return student
    
    def __str__(self):
        students_list = ""
        for student in self.students:
            students_list += f"{student.surname}, "
        students_list += '\n'
        students_list = students_list.replace(', \n', '')
        return students_list