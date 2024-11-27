import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('data.csv')

# Вычисление средней зарплаты
average_salary = data['salary'].mean()
print(f"Средняя зарплата сотрудников: {average_salary:.2f}")

# Отбор сотрудников старше 30 лет
employees_above_30 = data[data['age'] > 30]
print("\nСписок сотрудников старше 30 лет:")
print(employees_above_30[['name', 'age', 'salary']])
