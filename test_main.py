import pytest
from main_res import SalaryEmployee, HourlyEmployee, Department

@pytest.fixture
def employees():
    return [
        SalaryEmployee(name="Bob", role="manager"),
        HourlyEmployee(name="Brenda", role="developer"),
        HourlyEmployee(name="Alex", role="intern"),
    ]

def test_find_managers(employees):
    company = Department()
    company.employees = employees

    managers = company.find_managers()

    assert managers == [SalaryEmployee(name="Bob", role="manager")]

def test_find_developers(employees):
    company = Department()
    company.employees = employees

    developers = company.find_developers()

    assert developers == [HourlyEmployee(name="Brenda", role="developer")]

def test_find_interns(employees):
    company = Department()
    company.employees = employees

    interns = company.find_interns()

    assert interns == [HourlyEmployee(name="Alex", role="intern")]


def test_pay_employee():
    company = Department()
    employee = HourlyEmployee(name='Tim', role='intern')

    pay_result = company.pay_employee(employee)

    assert pay_result == 'Paying Tim $500'


    employee = SalaryEmployee(name='Bob', role='developer')
    pay_result = company.pay_employee(employee)

    assert pay_result == 'Paying Bob a monthly salary: $5000'


