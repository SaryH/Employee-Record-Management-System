from Employee import Employee


class Academic(Employee):
    def __init__(self, ID: int, Name, DateOfBirth, MartialStatus, Children, Gender, ContactInfo, Type, Status,
                 Department, StartingTime, BasicSalary, HealthInsurance, Semester, Year, Courses):
        super().__init__(ID, Name, DateOfBirth, MartialStatus, Children, Gender, ContactInfo, Type, Status, Department,
                         StartingTime, BasicSalary, HealthInsurance)
        self.experience = {}
        self.experience[Year, Semester] = Courses
        self.Semester = Semester
        self.Year = Year
        self.Courses = Courses

    def get_Semester(self):
        return self.Semester

    def set_Semester(self, x):
        self.Semester = x

    def get_Year(self):
        return self.Year

    def set_Year(self, x):
        self.Year = x

    def get_Courses(self):
        return self.Courses

    def set_Courses(self, x):
        self.Courses = x