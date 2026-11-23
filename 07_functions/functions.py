#Первая функция
#Создай функцию say_hello(), которая выводит Привет, мир!. Вызови её три раза.
def say_hello():
    print("Привет, мир!")
say_hello()
say_hello()
say_hello()
#Функция с параметром
#Создай функцию greet_user(name), которая выводит Привет, <имя>!.
#Вызови её для трёх разных имён, а затем для всех имён из списка users = ["Vadim", "Alex", "Max", "Daniel"] через цикл.
def greet_user(name):
    print(f"Привет, {name}!")
greet_user("Nikita")
greet_user("Sergey")
greet_user("Roma")
users= ["Vadim", "Alex", "Max", "Daniel"]
for user in users:
    greet_user(user)
#Два параметра
#Создай две функции:
#print_sum(a, b) — выводит a + b = результат.
#print_area(width, height) — выводит площадь прямоугольника в формате Площадь: 24.
#Вызови каждую хотя бы с двумя разными наборами чисел.
def print_sum(a, b):
    print(f"{a} + {b} = {a+b}")
def print_area(width, height):
    print(f"площадь прямоугольника в формате Площадь: {width*height}")
print_sum(1,3)
print_area(34,67)
#Функция с циклом
#Создай две функции:
#print_table(number) — выводит таблицу умножения на number от 1 до 10. Вызови для 3 и для 7.
#print_rectangle(rows, cols) — выводит прямоугольник из звёздочек нужного размера. Вызови для (4, 6) и для (2, 10).
def print_table(number):
    print("Таблица умножения:")
    for num in range(1,11):
        print(f"{num} * {number} = {num*number}")
print_table(3)
print_table(7)
def print_rectangle(rows, cols):
    print("Прямоугольник из звёздочек")
    for i in range(rows):
        print("*"*cols)
print_rectangle(4,6)
print_rectangle(2,10)
#Чек и оценка
#Создай две функции:
#print_receipt(shop, product, price, quantity) — выводит аккуратный чек в стиле твоего «Дубрава»:
#название магазина, товар, цена с двумя знаками после точки, количество, итог и благодарность. Вызови два раза для разных магазинов и товаров.
#print_grade(score) — по баллу выводит Excellent, Good, Average, Failed или Invalid score (условия те же, что в conditions_practice.py).
#Вызови для списка баллов [95, 80, 65, 30, 120] через цикл.
#Подсказка: логику ты уже писал, здесь задача — аккуратно «упаковать» её в функцию и убрать все числа, которые теперь приходят через параметры.
def print_receipt(shop, product, price, quantity):
    print(f"""{'='*10} ЧЕК {'='*10}
    
Добро пожаловать: {shop}
Товар: {product}
Цена товара: {price:.2f}
Количество: {quantity}

Итог: {price*quantity:.2f}

    Спасибо за покупку!""")
print_receipt("«Дубрава»","Кресло «Тихон»",14900,2)
print_receipt("LiveNNov","Молоко (1 л)",97,4)

def print_grade(score):
    if 0 <= score <= 59:
        print('Оценка: Failed')
    elif 60 <= score <= 74:
        print('Оценка: Average')
    elif 75 <= score <= 89:
        print('Оценка: Good')
    elif 90 <= score <= 100:
        print('Оценка: Excellent')
    else:
        print('Оценка: Invalid score')

score=[95, 80, 65, 30, 120]
for i in score:
    print_grade(i)