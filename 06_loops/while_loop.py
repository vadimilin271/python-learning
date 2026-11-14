#Счётчик
#Используя while, выведи числа от 1 до 10.
from traceback import print_tb

count = 1
while count != 11:
    print(count)
    count+=1
#Обратный отсчёт
#Выведи числа от 10 до 1, а после цикла выведи "Старт!".
count = 10
while count != 0:
    print(count)
    count -= 1
print("Старт!")
#Сумма чисел
#Используя while, посчитай сумму чисел от 1 до 100.
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)
#Поиск числа
#Дано:
#numbers = [4, 8, 15, 16, 23, 42]
#Используя while:
#- Перебери список.
#- Выведи каждый элемент.
#- Найди число 16 и останови цикл, когда найдёшь его.
#Подсказка: для перебора списка можно использовать индекс.
numbers = [4, 8, 15, 16, 23, 42]
i = 0
while i < len(numbers):
    print(numbers[i])
    if numbers[i] == 16:
        break
    i += 1
#Система попыток
#Создай переменную:
#secret_number = 7
#Пользователь должен вводить число, пока не угадает загаданное.
#- Если число меньше загаданного — выведи "Больше!".
#- Если больше — выведи "Меньше!".
#- Если угадал — выведи "Правильно!".
#Используй while и input().
secret_number = 7
while True:
    num = int(input("Ввелите число: "))
    if num < secret_number:
        print("Больше!")
    elif num > secret_number:
        print("Меньше!")
    else:
        print("Правильно!")
        break
