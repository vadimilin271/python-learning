#Задание №1. Информация о пользователе
#Создай переменные:
#- name — твоё имя.
#- age — возраст.
#- city — город.
#- height — любое значение типа float.
#- is_learning_python — логическое значение.
name = "Vadim"
age = 18
city = "Cheboksary"
height = 1.77
is_learning_python = True
print(name)
print(age)
print(city)
print(height)
print(is_learning_python)
#Задание №2. Типы данных
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
#Задание №3. Математика
#Создай две числовые переменные
#Выведи результаты всех семи математических операций.
a = 17
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#Задание №4. Преобразование типов
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
#Задание №5. Предскажи результат
x = 10
y = "5"

print(x + int(y))
print(str(x) + y)
print(x / 2)
print(x // 3)
print(x % 3)
print(type(y))
#выйдет 1) 15 2) 105 3) 5 4) 3 5) 1 6) str (делал сам честно)
#Задание №6. Мини-калькулятор магазина
#Есть данные:
#- Название товара.
#- Цена одного товара.
#- Количество купленных товаров.
#- Скидка в процентах.
#Тебе нужно самостоятельно:
#1. Создать переменные для хранения данных.
#2. Рассчитать стоимость без скидки.
#3. Рассчитать размер скидки.
#4. Рассчитать итоговую стоимость.
#5. Вывести красивый отчёт через f-строки.
product="Coca-Cola"
price = 85
quantity = 6
discount = 9
subtotal = price * quantity
discount_amount = (price * discount)/100
final_price = subtotal - (discount_amount*quantity)
print(f"Стоимость {product}: {price}, количество {product}: {quantity} скидка на {discount_amount:.2f}\nобщая стоимость {product}: {subtotal}\n{product} с сидкой: {final_price}")
#Задание №7. Обмен значениями
#Создай две переменные
#Сделай так, чтобы после выполнения программы значение поменялось нооборот
a = 10
b = 25
new_a = a
new_b = b
a = new_b
b = new_a
print(a)
print(b)
#Задание №8. Работа с данными
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
#Задание №9. Задача на логику
#У тебя есть: total_seconds = 7385
#Переведи это количество секунд в часы, минуты и оставшиеся секунды.
total_seconds = 7385
hours = total_seconds // 3600
minutes = (total_seconds % 3600)//60
seconds = total_seconds % 60
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")