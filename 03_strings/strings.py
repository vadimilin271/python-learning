#Создание профиля пользователя
#Создай переменные:
#- first_name
#- last_name
#- age
#- city
#Выведи их по отдельности, а затем выведи полное имя, объединив имя и фамилию.
first_name = 'Vadim'
last_name = "Ilin"
age = 18
city= "Cheboksary"
print(first_name)
print(last_name)
print(age)
print(city)
print(first_name+last_name)
#Объединение текста
#Создай три переменные со словами:
#word1 = "Python"
#word2 = "is"
#word3 = "awesome"
#Объедини их в одну строку с пробелами и выведи результат.
word1 = "Python"
word2 = "is"
word3 = "awesome"
print(word1,word2,word3)
#Длина текста
#Создай переменную:
#message = "I am learning Python"
#Выведи:
#- Сам текст.
#- Количество символов.
#- Тип данных переменной.
message = "I am learning Python"
print(message)
print(len(message))
print(type(message))
#Повторение строки
#Создай переменную separator, содержащую символ -.
#Выведи этот символ 30 раз, используя умножение строк.
separator = '-'
print(separator*30)
#Проверка типов
#Создай три переменные:
#number = 100
#number_text = "100"
#text = "Python"
#Выведи тип каждой переменной и объясни для себя, почему первые две имеют разные типы.
number = 100
number_text = "100"
text = "Python"
print(type(number))
print(type(number_text))
print(type(text))
#number имеет другой тип от number_text, потому что в number_text 100 находится в ковычках, а ковычки присваивают тип str