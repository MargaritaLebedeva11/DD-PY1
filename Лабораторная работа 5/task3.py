import random as rd

# Не совсем уверена, можно ли использовать прекрасную функцию sample из пакета random,
# которая, собственно, и создает список уникальных чисел из диапазона
def get_unique_list_numbers() -> list[int]:
    return rd.sample(range(-10, 10), 15)


# Поэтому написала функцию без использования sample. Но с ней, конечно, намного проще
def unique_list_numbers() -> list[int]:
    list2_ = []
    while len(list2_) != 15:
        num = rd.randint(-10, 10)
        if num not in list2_:
            list2_.append(num)

    return list2_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

unique_numbers = unique_list_numbers()
print(unique_numbers)
print(len(unique_numbers) == len(set(unique_numbers)))