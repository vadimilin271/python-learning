#Добавление пользователей
#Создай список из трёх пользователей.
#- Добавь четвёртого через append().
#- Добавь ещё одного пользователя на вторую позицию через insert().
#- Выведи результат.
users = ["Алексей Смирнов","Елена Ковалева","Дмитрий Петров"]
users.append("Мария Соколова")
users.insert(1,"Иван Новиков")
print(users)
#Работа с числами
#Создай список:
#numbers = [5, 2, 8, 2, 10, 2, 4]
#- Посчитай, сколько раз встречается 2.
#- Найди индекс числа 10.
#- Отсортируй список по возрастанию.
#- Затем отсортируй по убыванию.
numbers = [5, 2, 8, 2, 10, 2, 4]
print(numbers.count(2))
print(numbers.index(10))
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
#Объединение списков
#Создай два списка:
#backend = ["Python", "Java"]
#frontend = ["JavaScript", "HTML", "CSS"]
#Объедини их с помощью extend() и выведи результат.
backend = ["Python", "Java"]
frontend = ["JavaScript", "HTML", "CSS"]
backend.extend(frontend)
full_stack = backend
print(full_stack)
#Мини-система управления товарами
#Создай список:
#products = ["laptop", "mouse", "keyboard"]
#Выполни последовательно:
#- Добавь monitor.
#- Добавь headphones в начало списка.
#- Удали mouse.
#- Посчитай количество товаров.
#- Отсортируй список по алфавиту.
#- Выведи итоговый список.
products = ["laptop", "mouse", "keyboard"]
products.append("monitor")
products.insert(0,"headphones")
products.remove("mouse")
print(len(products))
products.sort()
print(products)
