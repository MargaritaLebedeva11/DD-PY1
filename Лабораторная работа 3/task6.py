list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max = list_numbers[0]
i = 0

for num in list_numbers:
    if num > max:
        max = num

index = list_numbers.index(max)
a = list_numbers[19]
list_numbers[19] = list_numbers[index]
list_numbers[index] = a

print(list_numbers)
