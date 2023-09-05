class EmployeeTable:
    def __init__(self):
        self.data = [
            {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
            {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
            {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
            {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
            {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000},
        ]

    def search_by_age(self, age):
        result = [employee for employee in self.data if employee["Age"] == age]
        return result

    def search_by_name(self, name):
        result = [employee for employee in self.data if employee["Name"].lower() == name.lower()]
        return result

    def search_by_salary(self, operator, salary):
        if operator == ">":
            result = [employee for employee in self.data if employee["Salary (PM)"] > salary]
        elif operator == "<":
            result = [employee for employee in self.data if employee["Salary (PM)"] < salary]
        elif operator == ">=":
            result = [employee for employee in self.data if employee["Salary (PM)"] >= salary]
        elif operator == "<=":
            result = [employee for employee in self.data if employee["Salary (PM)"] <= salary]
        else:
            result = []
        return result

    def display_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            print("Employee ID\tName\tAge\tSalary (PM)")
            for employee in results:
                print(f"{employee['Employee ID']}\t{employee['Name']}\t{employee['Age']}\t{employee['Salary (PM)']}")


def main():
    employee_table = EmployeeTable()

    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        age = int(input("Enter age to search: "))
        results = employee_table.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        results = employee_table.search_by_name(name)
    elif choice == 3:
        operator = input("Enter salary operator (> or < or >= or <=): ")
        salary = int(input("Enter salary to compare: "))
        results = employee_table.search_by_salary(operator, salary)
    else:
        print("Invalid choice.")
        return

    employee_table.display_results(results)


if __name__ == "__main__":
    main()
