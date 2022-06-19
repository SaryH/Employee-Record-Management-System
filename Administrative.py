from Employee import Employee


class Administrative(Employee):
    def __init__(self, ID: int, Name, DateOfBirth, MartialStatus, Children, Gender, ContactInfo, Type, Status,
                 Department, StartingTime, BasicSalary, HealthInsurance, Year, VacationDays):
        super().__init__(ID, Name, DateOfBirth, MartialStatus, Children, Gender, ContactInfo, Type, Status, Department,
                         StartingTime, BasicSalary, HealthInsurance)
        self.Year = Year
        self.VacationDays = VacationDays
        self.vacations = {}
        self.vacations[Year] = int(VacationDays)
        self.VacationDays = VacationDays

    def get_Year(self):
        return self.Year

    # setter method
    def set_Year(self, x):
        self.Year = x

    # getter method
    def get_VacationDays(self):
        return self.VacationDays

    # setter method
    def set_VacationDays(self, x):
        self.VacationDays = x
