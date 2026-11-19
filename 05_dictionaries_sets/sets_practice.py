#Список словарей
#Дан список:
#students = [
#    {"name": "Vadim", "grade": 85},
#    {"name": "Alex", "grade": 92},
#    {"name": "Max", "grade": 78},
#]
#Выведи:
#Имя второго студента.
#Каждого студента в формате Vadim: 85.
#Среднюю оценку.
students = [
    {"name": "Vadim", "grade": 85},
    {"name": "Alex", "grade": 92},
    {"name": "Max", "grade": 78},
]
print(f"Имя второго студента {students[1]['name']}")
total = 0
count = 0
for student in students:
    print(f"{student['name']}: {student["grade"]}")
    total += student["grade"]
    count +=1
avg = total/count
print(f"Среднюю оценка: {avg:.2f}")
#Вложенный словарь
#Дан словарь:
#employee = {
#    "name": "Ivan",
#    "position": "Developer",
#    "contacts": {"email": "ivan@mail.com", "phone": "12345"}
#}
#Выведи email, обратившись через два ключа.
#Измени телефон на "99999".
#Добавь в contacts новый ключ city со значением "Cheboksary".
#Выведи весь словарь.
employee = {
    "name": "Ivan",
    "position": "Developer",
    "contacts": {"email": "ivan@mail.com", "phone": "12345"}
}
print(f"email {employee['contacts']['email']}")
employee["contacts"]['phone'] = "99999"
employee["contacts"].setdefault("city","Cheboksary")
print(employee)
#Генератор словаря
#Дан список имён: names = ["vadim", "alex", "max"].
#Создай словарь, где ключ — имя, а значение — длина имени, через генератор словаря: {'vadim': 5, 'alex': 4, 'max': 3}.
#Создай второй словарь только из имён длиннее 3 символов.
names = ["vadim", "alex", "max"]
my_dict = {kay: len(kay) for kay in names}
len_dict = {key: len(key) for key in names if len(key)>3}
print(my_dict)
print(f"Словарь только из имён длиннее 3 символов: {len_dict}")
#Фильтрация записей
#Используя список students из первого задания (добавь ещё двух студентов на свой вкус):
#Выведи только тех, у кого оценка выше 80.
#Создай множество всех оценок.
#Найди студента с лучшей оценкой, max() нельзя.
students = [
    {"name": "Vadim", "grade": 85},
    {"name": "Alex", "grade": 92},
    {"name": "Max", "grade": 78},
    {"name": "Alexey", "grade": 88},
    {"name": "Maria", "grade": 95}
]
set_student =set()
best_grade = students[0]["grade"]
best_name = students[0]["name"]
for student in students:
    if student["grade"] > 80:
        print(f"Те, у кого оценка выше 80: {student}")
    set_student.add(student["grade"])
    if student["grade"]>best_grade:
        best_grade = student["grade"]
        best_name = student["name"]
print(f"Множество всех оценок {set_student}")
print(f"Студент с лучшей оценкой: {best_name}, с баллом: {best_grade}")
#Мини-склад
#Дан склад:
#warehouse = [
#    {"product": "laptop", "price": 1200, "quantity": 5},
#    {"product": "mouse", "price": 25, "quantity": 0},
#    {"product": "keyboard", "price": 80, "quantity": 12},
#    {"product": "monitor", "price": 300, "quantity": 3},
#]
#Выведи общую стоимость склада (цена × количество по каждому товару, затем сумма).
#Выведи названия товаров, которых нет в наличии (quantity == 0).
#Создай словарь {название: стоимость позиции} через генератор словаря.
#Добавь новый товар headphones (цена 150, количество 7) в список и выведи, сколько теперь позиций на складе.
warehouse = [
    {"product": "laptop", "price": 1200, "quantity": 5},
    {"product": "mouse", "price": 25, "quantity": 0},
    {"product": "keyboard", "price": 80, "quantity": 12},
    {"product": "monitor", "price": 300, "quantity": 3},
]
no_quantity = []
total= 0
for price in warehouse:
    price_cost =(price["price"] * price["quantity"])
    total += price_cost
    if price["quantity"] == 0:
        no_quantity.append(price["product"])
print(f"Общая стоимость склада: {total}")
print(f"Товароы, которых нет в наличии - {no_quantity}")
new_dict = {position["product"]: position["price"] * position["quantity"] for  position in warehouse}
print(new_dict)
warehouse.append({"product": "headphones", "price": 150, "quantity": 7})
print(f"Сколько позиций на складе: {len(warehouse)}")




