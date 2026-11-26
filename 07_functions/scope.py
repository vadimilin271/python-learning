#Локальная переменная
#Создай функцию calculate(), внутри которой переменная result = 10 * 5, и выведи её внутри функции.
#Вызови функцию. Затем снаружи попробуй вывести result, раскомментируй строку, прочитай NameError, потом закомментируй обратно.
# В комментарии объясни, почему ошибка.
def calculate():
    result = 10 * 5
    print(result)
#print(result)
#NameError: name 'result' is not defined, ошибка выходит потому что пайтоне не видит переменую , которая вызывается, ведь она находится в функции и то есть она локальная и толко испозуется в функции
calculate()
#Чтение глобальной
#Создай глобальную переменную discount = 15.
#Создай функцию show_discount(), которая выводит Скидка: 15%, используя глобальную переменную без передачи в параметры.
#Вызови два раза. Измени discount на 20 и вызови снова: результат должен измениться.
discount = 15
def show_discount():
    print(f"Скидка: {discount}%")
show_discount()
discount = 20
show_discount()
#Предскажи результат
#Не запуская код, запиши в комментариях, что выведет каждая строка, а потом проверь:
x = 10
def func1():
    x = 20
    print(x)
def func2():
    print(x)
def func3(x):
    x = x + 5
    print(x)
func1()
func2()
func3(100)
print(x)
#Если предсказание не совпало, объясни в комментарии почему.
#я думаю что  func1() выведет 20, func2() выведет 10, func3(100) выведет 105 и последнее print(x) выведет 10, и я прав
#Исправление через return
#Дан код:
#balance = 1000
#def withdraw(amount):
#    balance = balance - amount
#    print(balance)
#withdraw(300)
#Запусти, запиши название ошибки и объясни её в комментарии.
#Исправь двумя способами. Первый: через global. Второй: чтобы функция принимала balance параметром и возвращала новый баланс,
#а в основной части кода писалось balance = withdraw(balance, 300).
#В комментарии напиши, какой способ лучше и почему.
balance = 1000
def withdraw(amount):
    global balance
    balance = balance - amount
    print(balance)
withdraw(300)

balance = 1000
def withdraw(balance,amount):
    return balance - amount
balance = withdraw(balance, 300)
print(balance)
#Счётчик покупок
#Создай глобальную переменную cart_total = 0.
#Напиши функцию add_to_cart(total, price, quantity), которая возвращает новую сумму корзины. Без global.
#Добавь в корзину три товара подряд:
#cart_total = add_to_cart(cart_total, 1500, 2)
#cart_total = add_to_cart(cart_total, 300, 1)
#cart_total = add_to_cart(cart_total, 80, 5)
#print(f"Итого: {cart_total:.2f}")
#Результат должен быть 3700.00.
#Затем сделай вторую версию, где функция add_to_cart_global(price, quantity) использует global cart_total, и добавь те же три товара.
#Сравни в комментарии две версии: в какой проще найти ошибку, если сумма вдруг окажется неправильной.
cart_total = 0
def add_to_cart(total, price, quantity):
    return total+ price * quantity
cart_total = add_to_cart(cart_total, 1500, 2)
cart_total = add_to_cart(cart_total, 300, 1)
cart_total = add_to_cart(cart_total, 80, 5)
print(f"Итого: {cart_total:.2f}")
cart_total = 0
def add_to_cart_global(price, quantity):
    global cart_total
    cart_total += price * quantity
add_to_cart_global(1500, 2)
add_to_cart_global(300, 1)
add_to_cart_global(80, 5)
print(f"Итого: {cart_total:.2f}")
#первый вариант через return для меня понятнее в отличие от global, и проще найти ошибку в первом варианте мы даем переменые для вызова каждой функции
#Бонус (необязательно): Перекрытие встроенных
#Напиши numbers = [3, 7, 1], затем max = 5, затем попробуй вызвать max(numbers).
#Прочитай ошибку и запиши в комментарии, что произошло.
#Потом удали переменную через del max и повтори вызов.
numbers = [3, 7, 1]
max = 5
#print(max(numbers))
#Вышла ошибка TypeError: 'int' object is not callable произошло то , что я хочу передать переменую max как за встроеную функцию и поэтому выводит ошибку
del max
print(max(numbers))