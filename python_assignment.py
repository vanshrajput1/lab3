class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def _init_(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, operator, age):
        result = []
        for emp in self.employees:
            if operator == ">" and emp.age > age:
                result.append(emp)
            elif operator == "<" and emp.age < age:
                result.append(emp)
            elif operator == ">=" and emp.age >= age:
                result.append(emp)
            elif operator == "<=" and emp.age <= age:
                result.append(emp)
        return result

    def search_by_salary(self, operator, salary):
        result = []
        for emp in self.employees:
            if operator == ">" and emp.salary > salary:
                result.append(emp)
            elif operator == "<" and emp.salary < salary:
                result.append(emp)
            elif operator == ">=" and emp.salary >= salary:
                result.append(emp)
            elif operator == "<=" and emp.salary <= salary:
                result.append(emp)
        return result

    def search_by_emp_id(self, emp_id):
        result = []
        for emp in self.employees:
            if emp.emp_id == emp_id:
                result.append(emp)
        return result

def main():
    db = EmployeeDatabase()

    emp1 = Employee("161E90", "Raman", 41, 56000)
    emp2 = Employee("161F91", "Himadri", 38, 67500)
    emp3 = Employee("161F99", "Jaya", 51, 82100)
    emp4 = Employee("171E20", "Tejas", 30, 55000)
    emp5 = Employee("171G30", "Ajay", 45, 44000)

    db.add_employee(emp1)
    db.add_employee(emp2)
    db.add_employee(emp3)
    db.add_employee(emp4)
    db.add_employee(emp5)

    while True:
        print("Options:")
        print("1: Search by Age")
        print("2: Search by Salary")
        print("3: Search by Employee ID")
        print("4: Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            operator = input("Enter operator (>, <, <=, >=): ")
            age = int(input("Enter age: "))
            results = db.search_by_age(operator, age)
        elif choice == "2":
            operator = input("Enter operator (>, <, <=, >=): ")
            salary = int(input("Enter salary: "))
            results = db.search_by_salary(operator, salary)
        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            results = db.search_by_emp_id(emp_id)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        if not results:
            print("No matching records found.")
        else:
            print("Matching records:")
            for emp in results:
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__== "_main_":
    main()