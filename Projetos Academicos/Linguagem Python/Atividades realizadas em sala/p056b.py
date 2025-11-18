from p056a import Employee,FulltimeEmployee,HourlyEmployee

if __name__ == "__main__":

    emp1 = FulltimeEmployee("João", "Silva", 1800.00)
    print("=== Funcionário em tempo integral ===")
    print("Nome completo:", emp1.full_name())
    print("Salário base:", emp1.get_base_salary())
    print("Salário total:", emp1.compute_salary())


    emp2 = HourlyEmployee("Maria", "Oliveira", 40, 50.00)
    print("\n=== Funcionário horista ===")
    print("Nome completo:", emp2.full_name())
    print("Horas trabalhadas:", emp2.get_hours_worked())
    print("Valor da hora:", emp2.get_hour_value())
    print("Salário total:", emp2.compute_salary())