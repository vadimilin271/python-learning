#Создание списка
#Создай список programming_languages с пятью языками программирования.
#Выведи:
#- Весь список.
#- Первый элемент.
#- Последний элемент.
#- Количество элементов.
programming_languages = ["Python","JavaScript","Java","C#","C++"]
print(programming_languages)
print(programming_languages[0])
print(programming_languages[-1])
print(len(programming_languages))
#Работа с индексами
#Создай список:
#numbers = [10, 20, 30, 40, 50, 60]
#Выведи второй, четвёртый и последний элементы. Затем измени второй элемент на 200.
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1],numbers[3],numbers[-1])
numbers[1] = 200
print(numbers)
#Изменение списка
#Создай список из пяти имён.
#- Замени третье имя.
#- Выведи обновлённый список.
#- Выведи количество элементов.
#- Проверь, есть ли в списке определённое имя через in.
names = ["Александр","Мария","Дмитрий","Екатерина","Алексей"]
names[2] = "Вадим"
print(names)
print(len(names))
print('Вадим' in names)
#Список пользователей
#Создай список пользователей:
#users = ["Vadim", "Alex", "Max", "Daniel", "Ivan"]
#Выведи:
#- Первого и последнего пользователя.
#- Всех пользователей, кроме первого.
#- Первые три имени.
#- Список в обратном порядке.
users = ["Vadim", "Alex", "Max", "Daniel", "Ivan"]
print(users[0],users[-1])
print(users[1:])
print(users[:3])
print(users[::-1])
#Задание на понимание
#Создай список товаров:
#products = ["laptop", "mouse", "keyboard"]
#Измени название mouse на gaming mouse, затем выведи обновлённый список и проверь, присутствует ли в нём gaming mouse.
products = ["laptop", "mouse", "keyboard"]
products[1] = "gaming mouse"
print(products)
if "gaming mouse" in products:
    print("Есть")
else:
    print("Нету")