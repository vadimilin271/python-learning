#Создание множества
#Создай множество из пяти разных языков программирования.
#Выведи:
#Всё множество.
#Количество элементов.
#Проверку, есть ли в нём "Python" (через in).
sets_programming = {"Python","JavaScript","C++","Java","C#"}
print(sets_programming)
print(len(sets_programming))
print("Python" in sets_programming)
#Убираем дубликаты
#Дан список:
#numbers = [4, 8, 4, 15, 8, 16, 23, 15, 42, 4]
#Преврати его в множество и выведи результат.
#Выведи, сколько элементов было в списке и сколько осталось уникальных.
#Преврати уникальные значения обратно в список и отсортируй по возрастанию.
numbers = [4, 8, 4, 15, 8, 16, 23, 15, 42, 4]
print(f"Список: {numbers}, длина {len(numbers)}")
unique_numbers = set(numbers)
print(f"Уникальный список: {list(unique_numbers)}, длина {len(unique_numbers)} ")
sorted_numbers  = sorted(unique_numbers)
print(f"По возростанию: {sorted_numbers}")
#Методы множества
#Создай множество colors = {"red", "green", "blue"}.
#Добавь "yellow".
#Добавь "red" ещё раз и объясни в комментарии, что произошло.
#Удали "green" через remove().
#Попробуй удалить "black" через discard() и объясни в комментарии, чем это отличается от remove().
#Выведи итоговое множество.
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.add("red")#ничего не произошло
colors.remove("green")
colors.discard("black")#если бы удаляли "black" через remove() ,то появилась бы ошибка, а через метод discard() ошибки нет и программа не останавливается
print(f"Итоговое множество: {colors}")
#Операции над множествами
#Даны два множества студентов, записавшихся на курсы:
#python_course = {"Vadim", "Alex", "Max", "Ivan"}
#java_course = {"Alex", "Daniel", "Ivan", "Oleg"}
#Выведи:
#Кто записан хотя бы на один курс.
#Кто записан на оба курса.
#Кто записан только на Python.
#Кто записан только на один курс (но не на оба).
python_course = {"Vadim", "Alex", "Max", "Ivan"}
java_course = {"Alex", "Daniel", "Ivan", "Oleg"}
print(f"Кто записан хотя бы на один курс: {python_course | java_course}")
print(f"Кто записан на оба курса: {python_course & java_course}")
print(f"Кто записан только на Python: {python_course - java_course}")
print(f"Кто записан только на один курс (но не на оба): {java_course ^ python_course}")
#Анализ текста
#Дана строка:
#text = "the quick brown fox jumps over the lazy dog the fox"
#Найди все уникальные слова и выведи их количество.
#Есть множество «стоп-слов»: stop_words = {"the", "over"}.
#Получи множество слов, из которого эти слова убраны (одной операцией над множествами, без цикла).
#Найди слова, которые встречаются в тексте больше одного раза.
#Это можно сделать циклом со словарём из прошлого урока или как-то иначе, выбери сам.
#В комментарии напиши, какой способ выбрал и почему.
text = "the quick brown fox jumps over the lazy dog the fox"
words = set(text.split())
print(f"Все уникальные слова: {words}, их количество: {len(words)}")
stop_words = {"the", "over"}
filtered_words= words - stop_words
print(f"Множество слов, из которого эти слова убраны: {filtered_words}")
word_counts= {}
for word in text.split():
    word_counts[word] = word_counts.get(word,0)+1 #Выбрал потому что он позволяет хранить пары слово: количесвто
for key,value in word_counts.items():
    if value > 1:
        print(key)
