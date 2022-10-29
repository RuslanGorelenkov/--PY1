money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = salary - spend
money_capital += delta
while money_capital >= 0:
    month += 1
    spend *= 1 + increase
    delta = salary - spend
    money_capital += delta

print(month)
