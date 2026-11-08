#Получение части строки
#text = "Programming"
#Выведи:
#- Первые три символа.
#- Символы с индекса 3 до 6.
#- Последние четыре символа.
text = "Programming"
print(text[:3])
print(text[3:6])
print(text[-4:])
#Пропуск символов
#word = "ABCDEFGHIJ"
#Выведи каждый второй символ, используя step.
word = "ABCDEFGHIJ"
print(word[::2])
#Работа с концом строки
#language = "Python"
#Выведи:
#- Последние три символа.
#- Все символы, кроме последних двух.
#- Строку без первого символа.
language = "Python"
print(language[-3:])
print(language[:-2])
print(language[1:])
#Переворот строки
#text = "Backend"
#Получи обратную строку, используя только срезы.
text = "Backend"
print(text[::-1])
#Самостоятельное предсказание
#Сначала запиши, что, по твоему мнению, выведет каждая команда:
#text = "PythonDeveloper"
#print(text[2:8])
#print(text[:6])
#print(text[-5:])
#print(text[::3])
#print(text[::-1])
#Выведет:
#thonDe
#Python
#loper
#PhDep
#repoleveDnohtyP (делал сам честно)