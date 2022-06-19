class Employee:
    def __init__(self, ID: int, Name, DateOfBirth, MartialStatus, Children, Gender, ContactInfo,
                Type, Status, Department, StartingTime, BasicSalary, HealthInsurance):
        self.ID=ID
        self.Name=Name
        self.DateOfBirth=DateOfBirth
        self.MartialStatus=MartialStatus
        self.Children=Children
        self.Gender=Gender
        self.ContactInfo=ContactInfo
        self.Type=Type
        self.Status=Status
        self.Department=Department
        self.StartingTime=StartingTime
        self.BasicSalary=BasicSalary
        self.HealthInsurance=HealthInsurance

    def get_ID(self):
        return int(self.ID)

    def set_ID(self, x):
        self.ID = x

    def get_Name(self):
        return self.Name

    def set_Name(self, x):
        self.Name = x

    def get_DateOfBirth(self):
        return self.DateOfBirth

    def set_DateOfBirth(self, x):
        self.DateOfBirth = x

    def get_MartialStatus(self):
        return self.MartialStatus

    def set_MartialStatus(self, x):
        self.MartialStatus = x

    def get_Children(self):
        return self.Children

    def set_Children(self, x):
        self.Children = x

    def get_Gender(self):
        return self.Gender

    def set_Gender(self, x):
        self.Gender = x

    def get_ContactInfo(self):
        return self.ContactInfo

    def set_ContactInfo(self, x):
        self.ContactInfo = x

    def get_Type(self):
        return str(self.Type)

    def set_Type(self, x):
        self.Type = x

    def get_Status(self):
        return self.Status

    def set_Status(self, x):
        self.Status = x

    def get_Department(self):
        return self.Department

    def set_Department(self, x):
        self.Department = x

    def get_StartingTime(self):
        return self.StartingTime

    def set_StartingTime(self, x):
        self.StartingTime = x

    def get_BasicSalary(self):
        return self.BasicSalary

    def set_BasicSalary(self, x):
        self.BasicSalary = x

    def get_HealthInsurance(self):
        return self.HealthInsurance

    def set_HealthInsurance(self, x):
        self.HealthInsurance = x
