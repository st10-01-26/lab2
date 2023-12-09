money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0
all_money = money_capital + salary
while spend < all_money:
    money_capital -= (spend - salary)
    all_money = money_capital + salary
    spend *= 1 + increase
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
