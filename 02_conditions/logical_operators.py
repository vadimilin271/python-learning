#Доступ к аккаунту
#Создай переменные username и password.
#Доступ разрешён, если:
#- Username равен "admin".
#- Password равен "python123".
#Используй and.
username = "admin"
password = "python123"
if username == "admin" and password == "python123":
    print("Доступ разрешён")
else:print("Доступ запрещен")
#Скидка в магазине
#Создай переменные total_price и has_discount_card.
#Покупатель получает скидку, если:
#- Покупка составляет минимум 1000.
#- Или у него есть карта постоянного покупателя.
#Используй or.
total_price = 999
has_discount_card = False
if total_price >= 1000 or has_discount_card == True:
    print("Покупатель получет скидку")
else:
    print("Не получет скидку")
#Проверка блокировки
#Создай is_blocked = False.
#Выведи Access allowed, если аккаунт не заблокирован.
#Используй not.
is_blocked = False
if not is_blocked:
    print("Access allowed")