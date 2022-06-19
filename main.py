import os.path
from Employee import Employee
from Academic import Academic
from Administrative import Administrative
from datetime import date

IDs = {}
Employees = []
Academics = []
Admins = []


def readData(f1, f2, f3):
    if not f1.endswith(".txt"):
        f1 += ".txt"
    if not f2.endswith(".txt"):
        f2 += ".txt"
    if not f3.endswith(".txt"):
        f3 += ".txt"
    # reading general attributes
    with open(f1) as file:
        lines = file.readlines()
    # remove first line
    lines.pop(0)
    for line in lines:
        record = line.split(";")
        if len(record) != 13:
            print("Error in file structure!")
            exit(-1)
        ID = int(record[0].strip())
        fullname = record[1].split(",")
        first = fullname[0].strip()
        middle = fullname[1].strip()
        last = fullname[2].strip()
        name = first + " " + middle + " " + last
        birthdate = record[2].strip()
        martialstatus = record[3].strip()
        children = record[4].strip()
        gender = record[5].strip()
        info = record[6].split(",")
        contactinfo = info[0].strip() + "," + info[1].strip() + "," + info[2].strip()
        type = record[7].strip()
        status = record[8].strip()
        department = record[9].strip()
        startingtime = record[10].strip()
        salary = record[11].strip()
        health = record[12].strip()
        # checking validity
        if ID <= 10000 or ID >= 99999:
            print("ID is invalid! Must be 5 digits only!")
            exit(-1)
        if int(ID) in IDs:
            print("Employee already exists!")
            exit(-1)
        IDs[int(ID)] = True
        if type.lower() != "academic" and type.lower() != "administrative":
            print("Employee type does not match neither academic nor administrative!")
            exit(-1)
        if status.lower() != "full-time" and status.lower() != "part-time" and status.lower() != "left-university":
            print("Employee status does not match neither part time, nor full time, nor left university!")
            exit(-1)
        if type.lower() == "academic":
            Employees.append(
                Employee(int(ID), name, birthdate, martialstatus, children, gender, contactinfo, type, status,
                         department,
                         startingtime, salary, health))
            Academics.append(
                Academic(int(ID), name, birthdate, martialstatus, children, gender, contactinfo, type, status,
                         department,
                         startingtime, salary, health, "", "", ""))
        else:
            Employees.append(
                Employee(int(ID), name, birthdate, martialstatus, children, gender, contactinfo, type, status,
                         department,
                         startingtime, salary, health))
            Admins.append(
                Administrative(int(ID), name, birthdate, martialstatus, children, gender, contactinfo, type, status,
                               department,
                               startingtime, salary, health, "", 0))
    # reading academic file
    with open(f2) as file:
        lines = file.readlines()
    lines.pop(0)
    for line in lines:
        record = line.split(";")
        if len(record) != 4:
            print("Error in Academic file structure!")
            exit(-1)
        ID = int(record[0].strip())
        semester = record[1].strip()
        year = record[2].strip()
        courses = record[3].split(" ")
        if not courses[0]:
            courses.pop(0)
        for i in range(0, len(courses)):
            courses[i] = courses[i].strip()
        if ID not in IDs:
            print("ID does not belong to anyone!")
            exit(-1)
        for employee in Academics:
            if employee.get_ID() == ID:
                employee.set_Year(year)
                employee.set_Semester(semester)
                employee.set_Courses(courses)
                employee.experience[year, semester] = courses
                break
    # reading admin file
    with open(f3) as file:
        lines = file.readlines()
    lines.pop(0)
    for line in lines:
        record = line.split(";")
        if len(record) != 3:
            print("Error in Administrative file structure!")
            exit(-1)
        ID = int(record[0].strip())
        year = record[1].strip()
        vacationdays = record[2].strip()
        if ID not in IDs:
            print("ID does not belong to anyone!")
            exit(-1)
        for employee in Admins:
            if employee.get_ID() == ID:
                employee.set_Year(year)
                employee.set_VacationDays(vacationdays)
                employee.vacations[year] = int(vacationdays)
                break


def checkFiles(f1, f2, f3):
    if not f1.endswith(".txt"):
        f1 += ".txt"
    if not f2.endswith(".txt"):
        f2 += ".txt"
    if not f3.endswith(".txt"):
        f3 += ".txt"
    return os.path.exists(f1) & os.path.exists(f2) & os.path.exists(f3)


def addEmployee():
    ID = int(input("Enter employee ID:"))
    while ID in IDs:
        ID = int(input("ID exists already, please provide another one:"))
    while ID <= 10000 or ID >= 99999:
        ID = int(input("ID is invalid! Enter 5 digits only:"))
    IDs[ID] = True
    first = input("Employee First Name:")
    middle = input("Employee Middle Name:")
    last = input("Employee Last Name:")
    name = first + " " + middle + " " + last
    birthdate = input("Employee Birthdate:")
    martialstatus = input("Employee Martial Status:")
    while martialstatus.lower() != "single" and martialstatus.lower() != "married":
        martialstatus = input("Do not say it is complicated! Either married or single:")
    children = input("Employee's number of Children:")
    gender = input("Employee Gender:")
    while gender.lower() != "male" and gender.lower() != "female":
        gender = input("What?? Biologically, you can only be either male or female:")
    email = input("Employee Email:")
    phone = input("Employee Phone number:")
    fax = input("Employee Fax:")
    contactinfo = email + "," + phone + "," + fax
    type = input("Employee Type:")
    while type.lower() != "academic" and type.lower() != "administrative":
        type = input("Wrong Employee Type! Enter either academic or administrative:")
    status = input("Employee Status:")
    while status.lower() != "full-time" and status.lower() != "part-time" and status.lower() != "left-university":
        status = input("Wrong employee status! Enter again:")
    department = input("Employee Department:")
    startingtime = input("Employee starting time:")
    salary = int(input("Employee Base Salary:"))
    health = input("Is Employee enrolled in health insurance?")
    while health.lower() != "true" and health.lower() != "false":
        health = input("Wrong answer! True or False:")
    Employees.append(
        Employee(ID, name, birthdate, martialstatus, children, gender, contactinfo, type, status, department,
                 startingtime, salary, health))
    if type.lower() == "academic":
        Academics.append(
            Academic(int(ID), name, birthdate, martialstatus, children, gender, contactinfo, type, status,
                     department,
                     startingtime, salary, health, "", "", ""))
    else:
        Admins.append(
            Administrative(int(ID), name, birthdate, martialstatus, children, gender, contactinfo, type, status,
                           department,
                           startingtime, salary, health, "", 0))


def updateEmployee():
    ID = int(input("Enter employee ID:"))
    if ID not in IDs:
        print("Employee does not exist!")
        return
    choice = ""
    while choice != "13":
        print("1. Name")
        print("2. Date of Birth")
        print("3. Martial Status")
        print("4. Children")
        print("5. Gender")
        print("6. Contact Info")
        print("7. Type")
        print("8. Status")
        print("9. Department")
        print("10. Starting Time")
        print("11. Basic Salary")
        print("12. Health Insurance")
        print("13. Return to Menu")
        choice = input("What do you want to Change?")
        type = ""
        if choice == "1":
            first = input("Employee First Name:")
            middle = input("Employee Middle Name:")
            last = input("Employee Last Name:")
            name = first + " " + middle + " " + last
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_Name(name)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_Name(name)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_Name(name)
                        break
        elif choice == "2":
            birthdate = input("Employee Birthdate:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_DateOfBirth(birthdate)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_DateOfBirth(birthdate)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_DateOfBirth(birthdate)
                        break
        elif choice == "3":
            martialstatus = input("Employee Martial Status:")
            while martialstatus.lower() != "single" and martialstatus.lower() != "married":
                martialstatus = input("Do not say it is complicated! Either married or single:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_MartialStatus(martialstatus)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_MartialStatus(martialstatus)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_MartialStatus(martialstatus)
                        break
        elif choice == "4":
            children = input("Employee's number of Children:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_Children(children)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_Children(children)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_Children(children)
                        break
        elif choice == "5":
            gender = input("Employee Gender:")
            while gender.lower() != "male" and gender.lower() != "female":
                gender = input("What?? Biologically, you can only be either male or female:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_Gender(gender)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_Gender(gender)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_Gender(gender)
                        break
        elif choice == "6":
            email = input("Employee Email:")
            phone = input("Employee Phone number:")
            fax = input("Employee Fax:")
            contactinfo = email + "," + phone + "," + fax
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_ContactInfo(contactinfo)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_ContactInfo(contactinfo)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_ContactInfo(contactinfo)
                        break
        elif choice == "7":
            newtype = input("Employee Type:")
            while newtype.lower() != "academic" and type.lower() != "administrative":
                newtype = input("Wrong Employee Type! Enter either academic or administrative:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    if type.lower() == newtype.lower():
                        print("Type not changed! you entered the same type! " + type)
                        return
                    employee.set_Type(newtype)
                    break
            if newtype.lower() == "academic":
                for employee in Admins:
                    if employee.get_ID() == ID:
                        Academics.append(Academic(employee.get_ID(), employee.get_Name(), employee.get_DateOfBirth(),
                                                  employee.get_MartialStatus(), employee.get_Children(),
                                                  employee.get_Gender(), employee.get_ContactInfo(), newtype,
                                                  employee.get_Status(), employee.get_Department(),
                                                  employee.get_StartingTime(), employee.get_BasicSalary(),
                                                  employee.get_HealthInsurance(), "", "", ""
                                                  ))
                        Admins.remove(employee)
                        break
            else:
                for employee in Academics:
                    if employee.get_ID() == ID:
                        Admins.append(Administrative(employee.get_ID(), employee.get_Name(), employee.get_DateOfBirth(),
                                                     employee.get_MartialStatus(), employee.get_Children(),
                                                     employee.get_Gender(), employee.get_ContactInfo(), newtype,
                                                     employee.get_Status(), employee.get_Department(),
                                                     employee.get_StartingTime(), employee.get_BasicSalary(),
                                                     employee.get_HealthInsurance(), "", 0
                                                     ))
                        Academics.remove(employee)
                        break
        elif choice == "8":
            status = input("Employee Status:")
            while status.lower() != "full-time" and status.lower() != "part-time" and status.lower() != "left-university":
                status = input("Wrong employee status! Enter again:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_Status(status)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_Status(status)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_Status(status)
                        break
        elif choice == "9":
            department = input("Employee Department:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_Department(department)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_Department(department)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_Department(department)
                        break
        elif choice == "10":
            startingtime = input("Employee starting time:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_StartingTime(startingtime)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_StartingTime(startingtime)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_StartingTime(startingtime)
                        break
        elif choice == "11":
            salary = int(input("Employee Base Salary:"))
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_BasicSalary(salary)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_BasicSalary(salary)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_BasicSalary(salary)
                        break
        elif choice == "12":
            health = input("Is Employee enrolled in health insurance?")
            while health.lower() != "true" and health.lower() != "false":
                health = input("Wrong answer! True or False:")
            for employee in Employees:
                if employee.get_ID() == ID:
                    type = employee.get_Type()
                    employee.set_HealthInsurance(health)
                    break
            if type.lower() == "academic":
                for employee in Academics:
                    if employee.get_ID() == ID:
                        employee.set_HealthInsurance(health)
                        break
            else:
                for employee in Admins:
                    if employee.get_ID() == ID:
                        employee.set_HealthInsurance(health)
                        break
        elif choice == "13":
            return
        else:
            print("Incorrect Choice!")


def updateAdmin():
    ID = int(input("Enter employee ID:"))
    if ID not in IDs:
        print("Employee does not exist!")
        return
    for employee in Admins:
        if employee.get_ID() == ID:
            if employee.get_Status().lower() == "left-university":
                print("Employee is no longer in University!")
                return
            if employee.get_Type().lower() != "administrative":
                print("Employee is not an Admin")
                return
            year = input("Enter year:")
            vacations = input("Enter number of vacations in " + year + ":")
            employee.vacations[year] = int(vacations)


def updateAcademic():
    ID = int(input("Enter employee ID:"))
    if ID not in IDs:
        print("Employee does not exist!")
        return
    for employee in Academics:
        if employee.get_ID() == ID:
            if employee.get_Status().lower() == "left-university":
                print("Employee is no longer in University!")
                return
            if employee.get_Type().lower() != "academic":
                print("Employee is not Academic")
                return
            year = input("Enter year:")
            semester = input("Enter semester:")
            numberofcourses = int(input("Enter number of courses:"))
            courses = []
            for i in range(0, numberofcourses):
                courses.append(input("Enter Course #" + str(i + 1)))
            employee.experience[year, semester] = courses


def displayStatistics():
    print("University has " + str(len(Academics)) + " Academic Employees")
    print("University has " + str(len(Admins)) + " Administrative Employees")
    fulltime = 0
    males = 0
    for employee in Employees:
        if employee.get_Gender().lower() == "male":
            males += 1
        if employee.get_Status().lower() == "full-time":
            fulltime += 1
    print("Percentage of full time employees: " + str(float(fulltime / len(Employees) * 100.00)) + "%")
    print("University has " + str(males) + " male employees")
    print("University has " + str(int(len(Employees) - males)) + " female employees")


def salaryStatistics():
    if len(Academics) == 0:
        print("There aren't exist Academic employees")
    else:
        AcademicTotal = 0
        AdmTotal = 0
        for employee in Employees:
            if employee.get_Type().lower() == 'academic':
                AcademicTotal += int(employee.get_BasicSalary()) + 15 * int(employee.get_Children())
                if employee.get_MartialStatus().lower() == 'married':
                    AcademicTotal += 20
                    if employee.get_HealthInsurance().lower() == 'true':
                        AcademicTotal -= 12 * (1 + int(employee.get_Children()))
            else:
                AdmTotal += int(employee.get_BasicSalary()) + 15 * int(employee.get_Children())
                if employee.get_MartialStatus().lower() == 'married':
                    AdmTotal += 20
                    if employee.get_HealthInsurance().lower() == 'true':
                        AdmTotal -= 12 * (1 + int(employee.get_Children()))
        print(
            "The average salary of Academic employees salaries is: " + str(float(1.0 * AcademicTotal / len(Academics))))
        print("The average salary of Administrative employees salaries is: " + str(float(1.0 * AdmTotal / len(Admins))))
        salary = int(input("Enter a salary to display the employees who get higher than: "))
        for employee in Employees:
            current1 = int(employee.get_BasicSalary()) + 15 * int(employee.get_Children())
            if employee.get_MartialStatus().lower() == 'married':
                current1 += 20
                if employee.get_HealthInsurance().lower() == 'true':
                    current1 -= 12 * (1 + (1 + int(employee.get_Children())))
            if current1 > salary:
                print(
                    "The employee {0} has a salary {1}, which is greater than {2}".format(employee.get_Name(), current1,
                                                                                          salary))


def yearsSince(startdate):
    current = date.today()
    return current.year - startdate.year - ((current.month,current.day) < (startdate.month,startdate.day))


def retirementInfo():
    remaining = int(input("Enter remaining work years:"))
    for employee in Employees:
        hiredate = employee.get_StartingTime()
        temp1 = hiredate.split("/")
        workedyears = yearsSince(date(int(temp1[1].strip()), int(temp1[0].strip()), 1))
        birthdate = employee.get_DateOfBirth()
        temp2 = birthdate.split("/")
        currentage = yearsSince(date(int(temp2[2].strip()), int(temp2[1].strip()), int(temp2[0].strip())))
        if workedyears < 35 and currentage < 65:
            if min(65 - currentage, 35 - workedyears) <= remaining:
                print("{0} has {1} working years left".format(employee.get_Name(),
                                                              min(65 - currentage, 35 - workedyears)))


def courseStatistics():
    count = {}
    taught = {}
    for employee in Academics:
        for a, b in employee.experience:
            for courses in employee.experience[a, b]:
                if courses in count:
                    count[courses] += 1
                else:
                    count[courses] = 1
                if courses in taught:
                    taught[courses].append(employee.get_ID())
                else:
                    taught[courses] = []
                    taught[courses].append(employee.get_ID())

    for a in taught:
        taught[a] = set(taught[a])
    for courses in count:
        print("The course {0} was offered {1} times and was taught by {2} academic employees".format(courses,
                                                                                                     count[courses],
                                                                                                     len(taught[
                                                                                                             courses])))


def adminStats():
    for employee in Admins:
        totalvacations = 0
        for year in employee.vacations:
            totalvacations += int(employee.vacations[year])
        startingtime = employee.get_StartingTime()
        temp = startingtime.split("/")
        yearsworked = yearsSince(date(int(temp[1].strip()), int(temp[0].strip()), 1))
        if yearsworked == 0:
            yearsworked = 1
        average = float(totalvacations / yearsworked)
        print("{0} took {1} vacations with an average of {2} vacations per year".format(employee.get_Name(),
                                                                                        totalvacations, average))


def academicStats():
    courses = {}
    semesters = {}
    for employee in Academics:
        for a, b in employee.experience:
            if employee.get_ID() in semesters:
                semesters[employee.get_ID()] += 1
            else:
                semesters[employee.get_ID()] = 1
            for course in employee.experience[a, b]:
                if employee.get_ID() in courses:
                    courses[employee.get_ID()].append(course)
                else:
                    courses[employee.get_ID()] = []
                    courses[employee.get_ID()].append(course)
    for temp in courses:
        name = ""
        for employee in Academics:
            if int(employee.get_ID()) == int(temp):
                name = employee.get_Name()
                break
        print("{0} taught {1} courses with an average of {2} courses per semester".format(name, len(set(courses[temp])), float(len(courses[temp]) / semesters[temp])))


def main():
    ga = input("Enter the General Attributes file name:")
    ac = input("Enter the Academic file name:")
    ad = input("Enter the Administrative file name:")
    if not checkFiles(ga, ac, ad):
        print("Could not locate files!")
        exit(-1)
    readData(ga, ac, ad)
    while True:
        print("1. Add a new employee record")
        print("2. Update general attributes")
        print("3. Add/update administrative employee attribute")
        print("4. Add/update academic employee attribute")
        print("5. Employee’s statistics")
        print("6. Salary statistics")
        print("7. Retirement information")
        print("8. Courses statistics")
        print("9. Administrative employees’ statistics")
        print("10. Academic employees’ statistics")
        print("11. Exit")
        choice = input("Enter Choice:")
        if choice == "1":
            addEmployee()
        elif choice == "2":
            updateEmployee()
        elif choice == "3":
            updateAdmin()
        elif choice == "4":
            updateAcademic()
        elif choice == "5":
            displayStatistics()
        elif choice == "6":
            salaryStatistics()
        elif choice == "7":
            retirementInfo()
        elif choice == "8":
            courseStatistics()
        elif choice == "9":
            adminStats()
        elif choice == "10":
            academicStats()
        elif choice == "11":
            print("Goodbye!")
            exit(0)
        else:
            print("Enter a valid option!")


main()