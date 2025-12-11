from dataclasses import dataclass
from typing import List, Any


@dataclass
class Employee:
    name: str
    role: str
    vacation_days: int = 25
    pay: float = 0.0

    def take_a_holiday(self, payout: bool):
        if payout:
            print(f"Employee {self.name} is taking a holiday with payout.")
        else:
            print(f"Employee {self.name} is taking a holiday without payout.")
        self.vacation_days -= 1
        if self.vacation_days < 0:
            print("Vacation days went negative!")

@dataclass
class HourlyEmployee(Employee):
    hourly_rate: float = 50
    amount: int = 10

@dataclass
class SalaryEmployee(Employee):
    monthly_salary: float = 5000
    bonus: float = 1000

class Department:
    def __init__(self):
        self.employees: List[Any] = []
        self.managers = []
        self.role_counts = {"manager": 0, "developer": 0, "intern": 0}

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            if employee.role in self.role_counts:
                self.role_counts[employee.role] += 1
        else:
            print("Employee already exists.")

    def find_managers(self):
        managers = []
        for employee in self.employees:
            if employee.role == "manager":
                managers.append(employee)

        return managers

    def find_developers(self):
        developers = []
        for employee in self.employees:
            if employee.role == "developer":
                developers.append(employee)

        return developers

    def find_interns(self):
        interns = []
        for employee in self.employees:
            if employee.role == "intern":
                interns.append(employee)

        return interns

    def pay_employee(self, employee: Employee):
        if isinstance(employee, SalaryEmployee):
            return f"Paying {employee.name} a monthly salary: ${employee.monthly_salary}"
        elif isinstance(employee, HourlyEmployee):
            return f"Paying {employee.name} ${employee.hourly_rate * employee.amount}"
        else:
            return f"Employee {employee.name} has no defined payment method."

    def total_payroll(self):
        total = 0
        for emp in self.employees:
            if isinstance(emp, SalaryEmployee):
                total += emp.monthly_salary
            elif isinstance(emp, HourlyEmployee):
                total += emp.hourly_rate * emp.amount
            else:
                total += 0
        return total

    def list_employees(self):
        for emp in self.employees:
            print(f"Employee: {emp.name}, Role: {emp.role}")
            if hasattr(emp, 'monthly_salary'):
                print(f"Salary: {emp.monthly_salary}")

    def useless_method(self):
        pass

    def employee_check(self, employee):
        return employee in self.employees