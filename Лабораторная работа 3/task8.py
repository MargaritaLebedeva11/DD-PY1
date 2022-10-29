money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
debt = 0

# Вариант 1. Пытаемся расходы покрыть ЗП, а только после этого пользоваться подушкой безопасности
while money_capital >= debt:
    debt = spend - salary
    money_capital = money_capital - debt
    spend = spend * 1.05
    month = month + 1

# Вариант 2. Пытаемся сначала расходы покрыть подушкой безопасности
money_capital = 10000
spend = 6000
money = 0 # некоторый остаток после покрытия долгов подушкой

money_capital = money_capital - spend #В первый месяц покрыли расходы подушкой
months = 1
while money >= 0: #Считаем, на сколько хватит оставшихся денег
    money_capital = money_capital - spend
    money = money + salary + money_capital
    spend = spend * 1.05
    months = months + 1

print(month)
print(months)