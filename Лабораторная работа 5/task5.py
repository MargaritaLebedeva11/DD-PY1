import random as rd


def get_random_password(n=8) -> str:
    list_ = rd.sample([str(i) for i in range(0, 10)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)], n)
    return ''.join(list_)


print(get_random_password())