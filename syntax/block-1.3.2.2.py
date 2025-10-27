"""
Попытка посчитать погрешность при 10**s разовом прибавлнеии
к нулю float значения 0.1
"""

x = 0
s = 6
r = 10**s
for i in range(r + 1):
    x += 0.1
    if i == r:
        z = x // 10 * 10
        y = x - z
        print(f"when i = {i}")
        print(f"x = {x}")
        print(f"z = {z}")
        print(f"y = {y}")
