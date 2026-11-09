#Изменение регистра
#text = "pYtHoN dEvElOpEr"
#Выведи текст в нижнем регистре, верхнем регистре и с заглавными первыми буквами слов.
text = "pYtHoN dEvElOpEr"
print(text.lower())
#Удаление пробелов
#text = "   Hello Python   "
#Используй strip(), lstrip() и rstrip(). Посмотри, чем отличаются результаты.
text = "   Hello Python   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
#Замена текста
#message = "I am learning Java"
#Замени Java на Python.
message = "I am learning Java"
print(message.replace("Java","Python"))
#Разделение и объединение
#text = "apple banana orange"
#Раздели строку методом split(), затем объедини полученный список через join() с разделителем -.
text = "apple banana orange"
text = text.split()
text = "-".join(text)
print(text)
#Поиск и проверка
#text = "Python is a popular programming language"
#Используй startswith(), endswith(), find() и count().
text = "Python is a popular programming language"
print(text.startswith("Python"))
print(text.startswith("Java"))
print(text.endswith("language"))
print(text.endswith("framework"))
print(text.find("popular"))
print(text.count("p"))
#Комплексная задача
#username = "   VADIM_Developer   "
#Нужно:
#- Удалить лишние пробелы.
#- Перевести текст в нижний регистр.
#- Заменить _ на пробел.
#- Сделать первые буквы слов заглавными.
#- Вывести итоговый результат.
username = "   VADIM_Developer   "
username=username.strip()
username=username.lower()
username=username.replace('_',' ')
username=username.title()
print(username)