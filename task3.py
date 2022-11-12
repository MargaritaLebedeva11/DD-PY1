# В условии сказано, что последний элемент удаляется всегда по умолчанию,
# поэтому результат может отличаться от того, который задан в PyCharm для проверки

# Выполняем задание в соответствии с указаниями в его условии: с помощью слайсирования
def delt(list_, index=None):
    if index is not None:
        list_ = list_[0:index] + list_[index + 1:len(list_)-1]
    else:
        list_ = list_[0:len(list_) - 1]
    return list_


print('Вариант 1')
print(delt([0, 0, 1, 2], index=0))
print(delt([0, 1, 1, 2, 3], index=1))
print(delt([0, 1, 2, 3, 4, 4]), "\n")


# Можно сделать немного проще и воспользоваться функцией pop, которая по номеру индекса удаляет элемент
def delete(list_, index=None):
    if index is not None:
        list_.pop(index)
        list_.pop(-1)
    else:
        list_.pop(-1)
    return list_


print('Вариант 2')
print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
