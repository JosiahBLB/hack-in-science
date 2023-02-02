class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades: list[float] = []

    def add_exam(self, grade: float):
        self.grades.append(grade)
        
    def get_mean(self):
        return sum(self.grades)/len(self.main)    

class School:
    def __init__(self, name: str):
        self.name = name
        self.students: list[str] = []
        
    def add_student(self, student: str):
        self.students.append(student)
        
    def get_mean(self):
        all_students = []
        for student in self.students:
            student = student()
            for grade in student.grades:
                all_students.append(grade)
        return sum(all_students)/len(all_students)
        
    def get_best_student(self):
        all_students = {}
        for student in self.students:
            student = student()
            all_students[student.name] = student.get_mean()
        return max(all_students)


class City:
    def __init__(self, name: str):
        self.name = name
        self.schools: list[str] = []
        
    def add_school(self, school: str):
        self.schools.append(school)
        
    def get_mean(self):
        all_schools = []
        for school in self.schools:
            school = school()
            for student in school.students:
                student = student()
                for grade in student.grades:
                    all_schools.append(grade)
        return sum(all_schools)/len(all_schools)
