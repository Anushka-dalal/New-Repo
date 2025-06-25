# hw task -> 
# student has features like name, roll and subjects with marks. There are 5 subjects for every students with some marks.
# student has one operation which will display percentage of student.
# use dictionary for subject and marks

class Student:
    def __init__(self,nm, r, **sub):
        self.name = nm
        self.roll = r
        self.subjects = sub

    def display(self):
        total = sum(self.subjects.values())
        percent = (total* 100) / 500
        print("Name of Student =", self.name)
        print("Roll No of Student =", self.roll)
        for s,m in self.subjects.items():
            print(f"Marks in {s} = {m}")
        print(f"Percentage of Student = {percent} %")            


s = Student("Anushka",1, Math=90, Science=85, English=88, History=92, Geography=89)
s.display()


# Output:-
# Name of Student = Anushka
# Roll No of Student = 1
# Marks in Math = 90
# Marks in Science = 85
# Marks in English = 88
# Marks in History = 92
# Marks in Geography = 89
# Percentage of Student = 88.8 %


