from person import Person

class Student(Person):
    """Represents a student at a university."""

    def __init__(self, first_name, last_name, major, university, gpa):
        super().__init__(first_name, last_name)
        self.major = major
        self.university = university
        self.gpa = gpa

    def introduce(self):
        super()._who()
        print(f"Hi, my name is {self.first_name} and I am a {self.major} major at {self.university}.")

    def adjust_gpa(self, amount=0):
        self.gpa += amount

    if __name__=='__main__':
        print("Student Class")
