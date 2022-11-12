main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""


def get_count_char(str_):
    # Создаём словарь, где ключи - это буква, содержащаяся в строке
    lower_reg = str_.lower()
    new_str = []
    for i in list(set(lower_reg)):
        if i.isalpha() is True:
            new_str.append(i)
    new_str.sort()
    new_dir = {new_str[j]: 0 for j in range(0, len(new_str), 1)}
    count = 0
    # Теперь считаем, количество каждой буквы в строке
    for j in new_dir.keys():
        for i in lower_reg:
            if i == j:
                count = count + 1
        new_dir[j] = count
        count = 0
    return new_dir


# Функция, которая определяет процентное соотношение букв в строке
# Проценты округлены до двух знаков после запятой
def get_procent(dir_):
    for i in dir_.keys():
        num = dir_[i]
        dir_[i] = round(((num / sum(dir_.values())) * 100), 2)
    return dir_


dir_result = get_count_char(main_str)
print(get_count_char(main_str))
print(get_procent(dir_result))
