#Проверка возраста
#Создай переменную age.
#- Если возраст 18 или больше — выведи Adult.
#- Иначе — Minor.
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
#Проверка числа
#Создай переменную number.
#Определи, является ли число положительным, отрицательным или равным нулю.
number = 67
if number == 0:
    print("Число равен нулю")
elif number > 0:
    print("Число является положительное")
else:
    print("Число является отрицательным")
#Температура
#Создай переменную temperature.
#- Выше 30 — Hot.
#- От 20 до 30 включительно — Warm.
#- От 10 до 19 включительно — Cool.
#- Ниже 10 — Cold.
#Используй if, elif, else.
temperature = 36.6
if temperature < 10:
    print("Cold")
elif 10 <= temperature <= 19:
    print("Cool")
elif 20 <= temperature <= 30:
    print("Warm")
elif temperature > 30:
    print("Hot")