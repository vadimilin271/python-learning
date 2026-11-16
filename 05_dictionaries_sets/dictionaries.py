#Создание словаря
#Создай словарь car с ключами brand, model, year (любые значения).
#Выведи:
#Весь словарь.
#Марку и год отдельно, через обращение по ключу.
#Количество пар в словаре.
car = {"brand":"Toyota",
       "model":"Camry",
       "year":2022}
print(car)
print(car["brand"],car["year"])
print(len(car))
#Изменение данных
#Дан словарь:
#product = {"name": "Laptop", "price": 1200, "quantity": 5}
#Увеличь цену до 1400.
#Добавь новый ключ category со значением "Electronics".
#Удали ключ quantity.
#Выведи итоговый словарь.
product = {"name": "Laptop", "price": 1200, "quantity": 5}
product["price"]=1400
product["category"] = "Electronics"
del product["quantity"]
print(product)
#Проверка ключа
#Дан словарь:
#user = {"name": "Alex", "age": 24, "city": "Moscow"}
#Проверь через in, есть ли ключ "email". Если есть, выведи его значение, если нет — выведи Email не указан.
#Сделай то же самое для ключа "city".
user = {"name": "Alex", "age": 24, "city": "Moscow"}
if "email" in user:
    print(user["email"])
else:
    print("Email не указан.")
if "city" in user:
    print(user["city"])
else:
    print("City не указан")
#Перебор словаря
#Дан словарь цен:
#prices = {"apple": 80, "banana": 60, "orange": 95, "milk": 70}
#С помощью цикла:
#Выведи каждую пару в формате apple стоит 80 руб.
#Выведи только товары дороже 65.
#Посчитай сумму всех цен.
prices = {"apple": 80, "banana": 60, "orange": 95, "milk": 70}
for kay,value in prices.items():
    print(f"{kay} стоит {value} руб.")
summ = 0
for kay, value in prices.items():
    if value > 65:
        print(kay,value)
    summ += value
print(f"Сумма всех цен: {summ}")
#Подсчёт символов
#Дана строка text = "programming".
#Создай пустой словарь и с помощью цикла заполни его так, чтобы ключ был буквой, а значение — сколько раз она встречается в строке.
#Ожидаемый результат (порядок может отличаться):
#{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
#Подсказка: для каждой буквы проверяй через in, есть ли она уже в словаре. Если нет, ставь 1, если есть — прибавляй 1.
new_dict = {}
for letter in "programming":
    if letter in new_dict:
        new_dict[letter] += 1
    else:
        new_dict[letter] = 1
print(new_dict)