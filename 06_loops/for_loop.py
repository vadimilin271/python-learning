#Вывод чисел
#Используя range(), выведи числа от 1 до 10.
for number in range(1,11):
    print(number)
#Обратный порядок
#Выведи числа от 10 до 1 в обратном порядке.
for num in range(11,0,-1):
    print(num)
#Таблица умножения
#Создай переменную number = 7.
#С помощью цикла выведи таблицу умножения на 7 от 1 до 10.
#Пример формата:
#7 x 1 = 7
#7 x 2 = 14
number = 7
for num in range(1,11):
    print(f"{number} x {num} = {number*num}")
#Работа со списком
#Дан список:
#numbers = [12, 5, 8, 21, 4, 17, 30, 9]
#С помощью цикла:
#- Выведи каждое число.
#- Выведи только числа больше 10.
#- Посчитай сумму всех чисел.
numbers = [12, 5, 8, 21, 4, 17, 30, 9]
for number in numbers:
    print(number)
for number in numbers:
    if number > 10:
        print(number)
total = 0
for number in numbers:
    total = total+number
print(total)
#Анализ пользователей
#Дан список:
#users = ["Vadim", "Alex", "Max", "Daniel", "Ivan"]
#С помощью цикла:
#- Выведи каждого пользователя с сообщением Привет, имя!.
#- Выведи только имена, длина которых больше 4 символов.
#- Посчитай, сколько всего пользователей в списке, используя цикл.
users = ["Vadim", "Alex", "Max", "Daniel", "Ivan"]
for name in users:
    print(f"Привет, {name}!")
for len_name in users:
    if len(len_name) > 4:
        print(len_name)
count = 0
for names in range(len(users)):
    count+= 1
print(count)
