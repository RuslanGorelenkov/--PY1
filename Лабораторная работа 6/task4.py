import json

INPUT_FILE = "input.csv"

# Реализуем конвертер из csv в json формат
def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[{dict}]:
    with open(filename) as f:
        table = []  # создаем пустой список
        for index, line in enumerate(f):
            # Получаем список из строки с файле, в которой не будет конечного символа '\n' и запятых
            list_ = line.strip(new_line).split(delimiter)
            # Если мы на первой строке, сохраняем как список заголовков
            if index == 0:
                heads = list_
                continue  # Возвращаемся в начало цикла for

            table.append({})  # Добавляем новый словарь в конец списка

            for i, _ in enumerate(heads):
                # Берем последний элемент списка (добавленный словарь)
                # Добавляем в него нужный элемент
                table[-1][heads[i]] = str_[i]  # причем i-ый заголовок это ключ, а i-ое число это значение
    return table  # функция возвращает список словарей

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))  # Распечатываем json строку с отступами равными 4.