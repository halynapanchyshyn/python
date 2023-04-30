import modul_person as m_p


class Student(m_p.Person):
    def __init__(self, sex, age, origin, surname):
        super().__init__(sex, age, origin)
        self.surname = surname

    def __str__(self):
        return f"Student : {super().__str__()}, surname = {str(self.surname)}"
