#Квадрат числа
#Создай функцию square(n), которая возвращает квадрат числа.
#Вызови её для трёх чисел.
# Результат первого вызова сохрани в переменную и выведи, результат второго выведи сразу через print(...), третий используй в выражении: square(5) + square(3).
def square(n):
    return n**2
#1
result = square(3)
print(result)
#2
print(square(5))
#3
print(square(5) + square(3))
#Чётное или нет
#Создай функцию is_even(number), которая возвращает True, если число чётное, и False, если нет.
# Проверь на списке [1, 4, 7, 10, 15] через цикл и выведи Число 4 чётное: True.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
my_list = [1, 4, 7, 10, 15]
for i in my_list:
    print(f"Число {i} чётное: {is_even(i)}")
#print и return
#Создай две функции:
#add_print(a, b), которая выводит сумму через print.
#add_return(a, b), которая возвращает сумму через return.
#Выполни:
#x = add_print(2, 3)
#y = add_return(2, 3)
#print(x)
#print(y)
#Сначала в комментарии предположи, что выведет каждая строка, потом запусти и сравни. Затем объясни своими словами, в чём разница.
def add_print(a, b):
    print(a+b)
def add_return(a, b):
    return a+b
x = add_print(2, 3)
y = add_return(2, 3)
print(x)
print(y)
#я думаю, что оба выведут 5 , но x = add_print(2, 3) и тут тоже выведится 5 то есть будет три 5 , ладно я не прав после увиденого, разница return от print() в том что print() только выводит , а с return можно работать дальше по коду, add_print не возвращает ничего, поэтому в x лежит None
#Итоговая цена
#Создай функцию calculate_total(price, quantity, discount=0), которая возвращает итоговую стоимость с учётом скидки в процентах.
#Вызови её три раза:
#Без скидки.
#Со скидкой 10%.
#Результат одного вызова сохрани в переменную, затем выведи «Итого: ...» с двумя знаками после точки.
def calculate_total(price, quantity, discount=0):
    return price*quantity * (1 - discount / 100)
print(calculate_total(1900,2))
print(calculate_total(1900,2,10))
result = calculate_total(1900,2)
print(f"Итого: {result:.2f}")
#Анализ списка
#Создай функцию analyze(numbers), которая принимает список чисел и возвращает три значения:
#минимальное, максимальное и среднее. min(), max() и sum() использовать нельзя, только цикл.
#Проверь на [12, 5, 8, 21, 4, 17, 30, 9] и выведи результат красиво, распаковав в три переменные:
#Минимум: 4
#Максимум: 30
#Среднее: 13.25
def analyze(numbers):
    max_number = numbers[0]
    min_number = numbers[0]
    total = 0
    count = 0
    for n in numbers:
        if n > max_number:
            max_number = n
        elif n < min_number:
            min_number = n
        count +=1
        total+=n
    avd_number = total/count
    return min_number,max_number,avd_number
numbers = [12, 5, 8, 21, 4, 17, 30, 9]
min_value,max_value,average = analyze(numbers)
print(f"""Минимум: {min_value}
Максимум: {max_value}
Среднее: {average}""")
#Бонус (необязательно): оценка через return
#Перепиши свою функцию print_grade(score) так, чтобы она называлась get_grade(score) и возвращала строку ("Excellent", "Good" и т.д.), а не печатала.
#Вызови её для списка баллов, а печатай уже в цикле снаружи. Так ты сам увидишь, чем «возвращающая» функция удобнее.
def get_grade(score):
    if 0 <= score <= 59:
        return 'Failed'
    elif 60 <= score <= 74:
        return'Average'
    elif 75 <= score <= 89:
        return'Good'
    elif 90 <= score <= 100:
        return'Excellent'
    else:
        return'Invalid score'
score=[95, 80, 65, 30, 120]
for i in score:
    print(get_grade(i))
