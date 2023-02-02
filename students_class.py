"""
Implement a Student, School, and a City classes like so:

[√]   Student, School, and City have a name attribute, given at initialization time.
[√]   A Student have an add_exam(grade) method, recording a new grade for him, as a float.
[√]   A School have an add_student(student) method.
[√]   A City have an add_school(school) method.
      Student, School, and City have a get_mean() method giving:
[√]      For the Student, the average of its results.
[√]      For the School, the average of the students averages.
[√]      For the City the average of the School averages.
[√]    School have a get_best_student() method, returning the best Student.
[√]    Cities have a get_best_school() and a get_best_student() methods, returning respectively a School and a Student..

"""

class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.grades: list[float] = []

    def add_exam(self, grade: float) -> None:
        self.grades.append(grade)
        
    def get_mean(self) -> float:
        return sum(self.grades)/len(self.grades)    

class School:
    def __init__(self, name: str) -> None:
        self.name = name
        self.students: list[Student] = []
        
    def add_student(self, student: Student):
        self.students.append(student)
        
    def get_mean(self) -> float:
        all_students: list[Student] = []
        for student in self.students:
            all_students.append(student.get_mean())
        return sum(all_students)/len(all_students)
        
    def get_best_student(self) -> str:
        all_students: dict[str, float] = {}
        for student in self.students:
            all_students[student.name] = student.get_mean()
        return max(all_students, key=all_students.get())

class City:
    def __init__(self, name: str) -> None:
        self.name = name
        self.schools: list[School] = []
        
    def add_school(self, school: School) -> None:
        self.schools.append(school)
        
    def get_mean(self) -> float:
        all_schools: list[float] = []
        for school in self.schools:
            all_schools.append(school.get_mean())
        return sum(all_schools)/len(all_schools)

    def get_best_student(self) -> Student:
        all_students: dict[str, float] = {}
        for school in self.schools:
            all_students.update(school.get_best_student())
        return max(all_students, key=all_students.get())

    def get_best_school(self) -> School:
        all_schools:dict[str, float] = {}
        for school in self.schools:
            all_schools[school] = school.get_mean()
        return max(all_schools, key=all_schools.get())


if __name__ == "__main__":
    paris = City('paris')
    hkis = School('hkis')
    paris.add_school(hkis)
    for student_name, student_grades in (('alice', (1, 2, 3)),
                                        ('bob', (2, 3, 4)),
                                        ('catherine', (3, 4, 5)),
                                        ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for grade in student_grades:
            student.add_exam(grade)
        hkis.add_student(student)
    print(paris.get_best_school().name)
    print(paris.get_best_student().name)