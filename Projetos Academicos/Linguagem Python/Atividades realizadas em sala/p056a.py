from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def set_first_name(self, new_name):
        self.first_name = new_name

    def set_last_name(self, new_name):
        self.last_name = new_name

    @abstractmethod
    def compute_salary(self):
        pass

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, base_salary=1500.00):
        super().__init__(first_name, last_name)
        self.base_salary = base_salary

    def get_base_salary(self):
        return self.base_salary

    def set_base_salary(self, new_base_salary):
        self.base_salary = new_base_salary

    def compute_salary(self):
        return self.base_salary + 200


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, hours_worked, hour_value=300.00):
        super().__init__(first_name, last_name)
        self.hours_worked = hours_worked
        self.hour_value = hour_value

    def get_hours_worked(self):
        return self.hours_worked

    def get_hour_value(self):
        return self.hour_value

    def set_hours_worked(self, new_hours_worked):
        self.hours_worked = new_hours_worked

    def set_hour_value(self, new_hour_value):
        self.hour_value = new_hour_value

    def compute_salary(self):
        return self.hours_worked * self.hour_value
