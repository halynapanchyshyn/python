class Person:
    def __init__(self, sex, age, origin):
        self.sex = sex
        self.age = age
        self.origin = origin
    def __str__(self):
        return f"sex = {str(self.sex)}, age = {str(self.age)}, origin = {str(self.origin)}"
