import random
import string # импортируем модуль string
def get_random_password(n=8) -> str: # по умолчанию 8 символов в пароле
    up_letters = string.ascii_uppercase # создаем строку из латинских букв верхнего регистра
    low_letters = string.ascii_lowercase # оздаем строку их латинских букв нижнего регистра
    digits = string.digits # создаем строку из цифр 0-9
    combined_string = up_letters + low_letters + digits # создаем строку, соединяя 3 предыдущие строки
    password_list = random.sample(combined_string, n) # создаем список из случайных символов этой строки
    password = "".join(password_list) # соединяем элементы списка в строку без пробелов
    return password




print(get_random_password())
