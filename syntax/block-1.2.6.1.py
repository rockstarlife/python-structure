"""
Задание: Вычисли площадь круга (π≈3.14, r=5: pi * r ** 2).
Добавь проверки: если r>0, выведи; else — "Ошибка". Используй все типы операторов.
Необходим для перехода к блоку 3.
"""

pi = 3.14
r = float(input("Write R of your circle: "))
if r > 0:
    s_circle = pi * r**2
    print(f"Area of your circle = {s_circle}")
else:
    print("Your circle suck!!!")
    print(f"What you fucking mean when you say R = {r}?!")
    print("Don't try to trick me you snicky man!")
