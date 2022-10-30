def get_count_char(str_):
    str_ = str_.lower()
    no_space_list = str_.split() # разделение строки по пробелу
    no_space_str = "".join(no_space_list) # сборка строки из списка без разделителя
    no_comma_list = no_space_str.split(",") # разделение полученной строки по запятой, то есть получится список без пробелов и запятых
    no_comma_str = "".join(no_comma_list) # сборка строки из списка без разделителя
    no_point_list = no_comma_str.split(".") # разделение полученной строки по точке, то есть получится список без пробелов, запятых и точек
    no_point_str = "".join(no_point_list) # сборка стрки из списка без разделителей
    no_sign_list = no_point_str.split("!") # разделение полученной строки по восклицательному знаку, то есть получится список из чистых слов
    letter_str = "".join(no_sign_list) # сборка строки из списка без разделителей, получится строка только из букв
    if letter_str.isalpha():
        list_letters = list(letter_str) # делаем список из строки
        letter_dict = {}
        DEFAULT_COUNT = 0
        for letter in list_letters:
            letter_dict[letter] = letter_dict.get(letter, DEFAULT_COUNT) + 1
    return letter_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

# Вторая функция, которая принимает словарь символов. Функция должна вернуть новый словарь,
# где количество каждого элемента заменено на процентное отношение ко всем символам.
letter_dict = get_count_char(main_str)

def get_percent_char(dict_):
    total_count = sum(dict_.values()) # суммируем значения словаря
    for letter, count in dict_.items():
        dict_[letter] = count / total_count * 100
        dict_[letter] = round(dict_[letter])
    return dict_


print(get_count_char(main_str))
