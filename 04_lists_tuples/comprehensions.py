#Квадраты чисел
#Создай список чисел от 1 до 10.
#С помощью List Comprehension создай новый список, в котором каждое число возведено в квадрат.
my_list = [1,2,3,4,5,6,7,8,9,10]
squares = [number**2 for number in my_list]
print(squares)
#Чётные числа
#Дан список:
#numbers = [1, 5, 8, 12, 15, 20, 23, 30]
#Создай новый список только с чётными числами.
numbers = [1, 5, 8, 12, 15, 20, 23, 30]
even_numbers = [number for number in numbers if number % 2 ==0]
print(even_numbers)
#Преобразование имён
#Дан список:
#names = ["vadim", "alex", "max", "daniel"]
#Создай новый список, где все имена будут написаны заглавными буквами.
names = ["vadim", "alex", "max", "daniel"]
upper_names = [name.upper() for name in names]
print(upper_names)
#Фильтрация товаров
#Дан список цен:
#prices = [100, 250, 50, 700, 120, 900, 300]
#Создай новый список, в котором останутся только цены больше 200.
prices = [100, 250, 50, 700, 120, 900, 300]
nuw_prices = [number for number in prices if number > 200]
print(nuw_prices)
#Задание на понимание
#Дан список:
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Создай новый список, используя List Comprehension:
#- Если число чётное — возведи его в квадрат.
#- Если нечётное — умножь его на 10.
#Например, для числа 2 получится 4, а для 3 — 30.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [num **2 if num % 2 ==0 else num *10 for num in numbers]
print(new_list)