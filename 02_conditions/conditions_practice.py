#Система оценок
#Есть переменная score от 0 до 100.
#Определи оценку:
#- 90–100 — Excellent.
#- 75–89 — Good.
#- 60–74 — Average.
#- 0–59 — Failed.
#- Если значение вне диапазона 0–100 — Invalid score.
score = 67
if 0 <= score <=59:
    print('Failed')
elif 60 <= score <=74:
    print('Average')
elif 75 <= score <= 89:
    print('Good')
elif 90 <= score <= 100:
    print('Excellent')
else:
    print('Invalid score')
#Банковская операция
#Есть переменные:
#balance = 1500
#withdrawal = 800
#is_blocked = False
#Нужно проверить:
#- Заблокирован ли аккаунт.
#- Достаточно ли денег для снятия.
#- Если всё хорошо — рассчитать новый баланс.
#- Если операция невозможна — объяснить причину.
#Используй вложенные условия или логические операторы.
balance = 1500
withdrawal = 800
is_blocked = False
#Через вложенные условия
if not is_blocked:
    if balance >= withdrawal:
        balance -= withdrawal
        print(balance )
    else:
        print("Недостаточно средств")
else:
    print("Аккаунт заблокирован")
balance = 1500
withdrawal = 800
is_blocked = False
#Через логические операторы
if is_blocked == True:
    print("Аккаунт заблокирован")
elif balance < withdrawal:
    print("Недостаточно средств")
else:
    balance -= withdrawal
    print(balance)
#Задача без подсказки
#Есть три переменные:
#a = 15
#b = 27
#c = 9
#Найди наибольшее число, используя условия.
#Запрещено использовать max().
a = 15
b = 27
c = 9
if a <= b <= c or b <= a <= c:
    print(f"Самое большое число {c}")
elif a <= c <= b or c <= a <= b:
    print(f"Самое большое число {b}")
elif c <= b <= a or b <= c <= a:
    print(f"Самое большое число {a}")