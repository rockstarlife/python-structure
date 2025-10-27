"""
Как работает while?
while True:
    print("hello")
Будет вечно цикить и спамить hello.
While False:
не будет работать.
"""

x = 0
y = 100
while y != 0:
    x += 1  # каждый цикл прибавляем +1 к x.
    y -= 1  # каждый цикл уменьшаеми y на 1.
    if y == 0:
        print(f"x = {x}")
        print(f"y = {y}")
