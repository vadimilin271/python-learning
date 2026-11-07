#Задание Математика
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
#Задание Предскажи результат
x = 10
y = "5"
print(x + int(y))
print(str(x) + y)
print(x / 2)
print(x // 3)
print(x % 3)
print(type(y))
#выйдет 1) 15 2) 105 3) 5 4) 3 5) 1 6) str (делал сам честно)
#Задание Мини-калькулятор магазина
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
#Задание Задача на логику
#У тебя есть: total_seconds = 7385
#Переведи это количество секунд в часы, минуты и оставшиеся секунды.
total_seconds = 7385
hours = total_seconds // 3600
minutes = (total_seconds % 3600)//60
seconds = total_seconds % 60
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")