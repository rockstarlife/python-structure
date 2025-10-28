"""
Как работает while?
while True:
    print("hello")
Будет вечно цикить и спамить hello.
While False:
    ...
не будет работать.
"""

# Программа переливания из y в x
print("Переливаем из x в y")
x = 0
y = 100
y_bak = y
x_bak = x
print(f"Сейчас x = {x}")
print(f"и в y = {y}\n")
while y != 0:
    x += 1  # каждый цикл прибавляем +1 к x.
    y -= 1  # каждый цикл уменьшаеми y на 1.
    if y == 0:
        print(f"x = {x}")
        print(f"y = {y}")
        if x == y_bak and y == x_bak:
            print("done")
