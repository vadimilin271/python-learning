#Обработка имени пользователя
#username = "   vAdIm_123   "
#Требуется:
#- Удалить пробелы.
#- Привести имя к нижнему регистру.
#- Заменить _ на пробел.
#- Вывести длину итоговой строки.
#- Вывести первый и последний символы.
username = "   vAdIm_123   "
username = username.strip()
print(username)
username = username.lower()
print((username))
username = username.replace("_"," ")
print(username)
print(f"Длина итоговой строки: {len(username)}")
print(f"Первый {username[0]} и последний символ: {username[-1]}")
#Проверка сообщения
#message = "Python is great for backend development"
#Используй:
#- startswith()
#- endswith()
#- find()
#- count()
#Проверь начало, конец, положение слова backend и количество букв e.
message = "Python is great for backend development"
print(message.startswith("Python"))
print(message.startswith("JavaScript"))
print(message.endswith("development"))
print(message.endswith("builder"))
print(message.find("is"))
print(message.find("backend"))
print(message.count("a"))
print(message.count("e"))
#Формирование пользовательского профиля
#Создай переменные:
#first_name = "Vadim"
#last_name = "Ilin"
#age = 18
#city = "Cheboksary"
#Сформируй красивое сообщение профиля, используя:
#- Объединение строк.
#- f-строки.
#- Методы строк.
#- len().
#- Индексацию.
first_name = "Vadim"
last_name = "Ilin"
age = 18
city = "Cheboksary"
print(f"""Меня зовут: {first_name+ " " +last_name}. Мне {age} лет, и я живу в городе {city}
Главные мысли в голове: {'Ищу ответы там, где другие видят тупик.'.upper()}
Мое имя не длиное, всего состоит из {len(first_name)} символов
Первая буква моего имени - '{first_name[0]}', а фамилии '{last_name[0]}'""")
#Мини-система обработки заказа
#Создай данные товара, обработай название через методы строк, рассчитай итоговую стоимость и выведи аккуратный чек.
#Используй всё, что изучили в Strings.
product_name = "    =Ноутбук=    "
base_price = 105000
discount_percent = 12
quantity = 2

product_name = product_name.strip()
product_name = product_name.upper()
product_name = product_name.replace("=","")

discount_price = (base_price * discount_percent)/ 100
final_price = base_price - (discount_price*quantity)

print("="*10,"чек".upper(),"="*10)
print()
print(f"Товар: {product_name}")
print(f"Цена: {base_price:.2f}")
print(f"Скидка: {discount_percent}%")
print()
print(f"Итоговая цена:".upper(),final_price)