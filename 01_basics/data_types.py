#Типы данных
#Создай пять переменных разных типов:
#int, float, str, bool, NoneType.
#Выведи их значения и типы через type().
age = 18
height = 1.77
name = "Vadim"
is_learning_python = True
result = None
print(age,type(age))
print(height,type(height))
print(name,type(name))
print(is_learning_python,type(is_learning_python))
print(result,type(result))
#Преобразование типов
#Создай переменные
#Преобразовать age в целое число.
#Преобразовать price в дробное число.
#Рассчитать общую стоимость трёх товаров.
#Вывести результат и его тип.
age = "21"
price = "19.99"
quantity = 3
age = int(age)
price = float(price)
result = price * quantity
print(result)
print(type(result))
#Работа с данными
#Есть переменные.
#Необходимо преобразовать данные в подходящие типы и вывести информацию.
name = "Alex"
age = "24"
salary = "2500.50"
age = int(age)
salary = float(salary)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: {salary}")