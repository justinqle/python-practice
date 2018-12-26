from person import Person
from student import Student

andrew = Person('Andrew', 'Le')
ben = Person('Ben', 'Landon')
justin = Student('Justin', 'Le', 'Computer Science', 'UMD', 3.0)
mutaz = Student('Mutaz', 'Ahmed', 'Mechanical Engineering', 'UMD', 3.5)

andrew.speak("Play Hollow Knight.")
ben.speak("Good luck at UMD!")
justin.introduce()
justin.speak("I refuse to play Hollow Knight. But thanks Ben!")
mutaz.introduce()
mutaz.speak("I love my roomie Justin!")

print(f"Justin's GPA: {justin.gpa}")
print(f"Mutaz's GPA: {mutaz.gpa}")
justin.adjust_gpa() # default GPA adjustment is 0
justin.adjust_gpa(1)
mutaz.adjust_gpa(amount=-0.5)
print(f"Justin's New GPA: {justin.gpa}")
print(f"Mutaz's New GPA: {mutaz.gpa}")
