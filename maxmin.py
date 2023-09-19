numbers = [1, 5, 9, 4, 10, 55, 8, -9]
minmax_list = []
max_num = numbers[0]
min_num = numbers[0]

for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

minmax_list.append(min_num)
minmax_list.append(max_num)

print(minmax_list)