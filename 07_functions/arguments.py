#Позиционные аргументы
#Создай функцию print_person(name, age, city), которая выводит Vadim, 18 лет, город Cheboksary.
# Вызови её для двух разных людей.
# Затем вызови специально с перепутанным порядком и посмотри, что получилось, объясни в комментарии, почему так.
def print_person(name, age, city):
    print(f"{name}, {age} лет, город {city}")
print_person(f"Vadim",18,"Cheboksary")
print_person(f"Max",19,"NewCheboksary")

print_person("Cheboksary","Vadim",18) #Python просто подставляет значения по очереди "Cheboksary" попало в name, "Vadim" — в age, а 18 — в city
#Именованные аргументы
#Вызови ту же функцию print_person тремя способами:
#полностью позиционно, полностью через имена в обратном порядке (city=..., age=..., name=...), и смешанно (первый позиционный, остальные именованные).
print_person("Алексей",28,"Нижний Новгород")
print_person(city="Нижний Новгород", age=28, name="Алексей")
print_person("Алексей", city="Нижний Новгород", age=28)
#Значения по умолчанию
#Создай функцию print_order(product, quantity=1, city="Cheboksary"), которая выводит
#Заказ: Ноутбук, количество 1, доставка в Cheboksary. Вызови её четырьмя способами:
#Только с названием товара.
#С товаром и количеством.
#С товаром и городом (количество оставь по умолчанию, используй имя параметра).
#Со всеми тремя аргументами.
def print_order(product, quantity=1, city="Cheboksary"):
    print(f"Заказ: {product}, количество {quantity}, доставка в {city}")
print_order("Ноутбук")
print_order("Ноутбук",5)
print_order("Ноутбук",city="NewCheboksary")
#1. Позиционные.
print_order("Ноутбук",1,"Cheboksary")
#2. Именованные (keyword).
print_order("Ноутбук",quantity=1,city="Cheboksary")
#3. Значения по умолчанию.
print_order("Ноутбук")
#Скидка
#Создай функцию print_price(price, discount=0), которая выводит цену и итоговую цену со скидкой в процентах.
#Если скидка не передана, пиши Скидки нет.
#Пример вызовов: print_price(1000) и print_price(1000, 15).
#Подсказка: условие if discount == 0 ты уже умеешь.
def print_price(price, discount=0):
    if discount == 0:
        print(f"Цена: {price} \nСкидки: нет")
    else:
        print(f"Цена: {price} \nСкидки: {discount} \nИтоговая цена(с скидкой) {price * (1 - discount / 100):.2f}")
print_price(1000)
print_price(1000, 15)
#Профиль и ошибки
#Создай функцию print_profile(name, age, city="не указан", is_student=False), которая выводит аккуратную анкету:
#Имя, возраст, город.
#Строка Статус: студент или Статус: не студент, в зависимости от is_student.
#Дальше:
#Вызови функцию тремя разными способами (минимум: только обязательные, с городом, со всеми четырьмя через имена).
#Допиши в комментариях, что произойдёт, если вызвать print_profile("Alex"). Не запускай заранее, сначала предположи, затем проверь и сравни.
#Закомментируй строку def print_profile(name, city="не указан", age, is_student=False) и объясни, почему Python не позволит так написать.
def print_profile(name, age, city="не указан", is_student=False):
    if is_student == False:
        print(f"""{"="*5}АНКЕТА{"="*5}
Имя - {name}
Возраст - {age}
Город - {city}
Статус - не студент""")
    else:
        print(f"""{"=" * 5}АНКЕТА{"=" * 5}
Имя - {name}
Возраст - {age}
Город - {city}
Статус - студент""")
#только обязательные
print_profile("Вадим",18,)
#с городом
print_profile("Вадим",18,"Чебоксары")
#со всеми четырьмя через имена
# со всеми четырьмя через имена
print_profile(name="Вадим", age=18, city="Чебоксары", is_student=True)
#при вывода print_profile("Alex") скорее всего вызовиится ошибка , потому что не передали значение age и поэтому пайтон не может его найти , но если бы записали имя и возраст ,то вышло бы я так думаю
#print_profile("Alex")
#TypeError: print_profile() missing 1 required positional argument: 'age'
#если закомментировать def print_profile(name, age, city="не указан", is_student=False): во 1 из за отстуов и во 2 нету переменых с которыми они работают
#def print_profile(name, city="не указан", age, is_student=False)
#Будет ошибка SyntaxError: при вызове значения идут по порядку, и 18 попадёт в city, а age останется пустым. Поэтому обычные параметры всегда ставят до параметров по умолчанию.

