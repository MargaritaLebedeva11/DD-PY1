salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# так как цены повышаются со второго месяца
months = months - 1

while months >= 0:
    need_money = need_money + (spend - salary)
    spend = spend * 1.03
    months = months - 1


print(round(need_money))
