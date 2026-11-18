#Безопасный доступ
#Дан словарь:
#user = {"name": "Alex", "age": 24, "city": "Moscow"}
#С помощью .get() выведи:
#Имя.
#Email. Если его нет, выведи Не указан.
#Телефон. Если его нет, выведи None (без второго аргумента).
user = {"name": "Alex", "age": 24, "city": "Moscow"}
print(user.get("name"))
print(user.get("email","Не указан"))
print(user.get("телефон"))
#Ключи и значения
#Дан словарь:
#scores = {"Vadim": 85, "Alex": 92, "Max": 78}
#Выведи отдельно:
#Все ключи.
#Все значения.
#Все пары.
#Преврати ключи в обычный список и выведи его.
scores = {"Vadim": 85, "Alex": 92, "Max": 78}
print(scores.keys())
print(scores.values())
print(scores.items())
keys_list = list(scores.keys())
print(keys_list)
#pop и update
#Дан словарь:
#product = {"name": "Phone", "price": 800, "stock": 10}
#Удали stock через pop() и выведи, какое значение вернулось.
#Через update() измени цену на 750 и добавь brand: "Samsung".
#Выведи итоговый словарь.
product = {"name": "Phone", "price": 800, "stock": 10}
stock = product.pop("stock")
print(stock)
product.update({"price":750,"brand":"Samsung"})
print(product)
#Копия словаря
#Создай словарь original = {"a": 1, "b": 2}.
#Сделай backup = original.copy().
#Измени original["a"] на 100.
#Выведи оба словаря и объясни в комментарии, почему backup не изменился.
original = {"a": 1, "b": 2}
backup = original.copy()
original["a"]=100
print(original)
print(backup)
#backup не изменился потому что мы сперва сделалаи копию, а потом толко изменили оригинал , то есть Python не види изменеие оригинала , а оригинал потом меняется и при выводе получается так
#Подсчёт слов
#Дана строка:
#text = "python is great and python is fun and fun is good"
#Раздели её на слова через split().
#С помощью цикла и .get() посчитай, сколько раз встречается каждое слово.
#Условия if/else использовать нельзя, всё в одну строку внутри цикла.
#Найди слово, которое встречается чаще всего, и выведи его с количеством.
# Функцию max() использовать нельзя, только цикл.
#Подсказка: counts[word] = counts.get(word, 0) + 1.
# Попробуй сам понять, почему это работает, и сравни с тем, как ты решал «Подсчёт символов».
text = "python is great and python is fun and fun is good"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1#ну я понял как работает это у нас есть текст ,нам нужен словарь , чтобы хранить ключи и их значения его создаем,
#перебираем каждое слово именно слово а не букву из за того что исползуем метод .split() разделили по словам и появился список и его перебираем
#в словрь записываем ключь каждое слово и значение 0 и если совподает то добовля к значение +1
#отличается Подсчёт слов от «Подсчёт символов» тем что исползуем .split() и смотрим ни не каждое букву ,а на слово
most_frequent_word = ""
max_count = 0
for word, count in counts.items():
  if count > max_count:
    max_count = count
    most_frequent_word = word
print(f"Самое частое слово: '{most_frequent_word}' (встречается {max_count} раз)")
