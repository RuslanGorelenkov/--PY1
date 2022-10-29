list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_number = list_numbers[0]
max_index = 0
for index, number in enumerate(list_numbers):
    if number > max_number:
        max_number = number
        max_index = index
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]
# -1 это индекс последнего элемента, ели начинать отсчет с конца последовательности

print(list_numbers)
