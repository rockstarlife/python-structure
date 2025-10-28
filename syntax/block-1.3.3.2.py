"""
continue - переводится как продолжать
что он делает?
if True:
    continue
здесь мы никогда не окажемся. так как continue постоянно
возвращет нас в начала программы внутри цикла.
"""

# Показательный пример
for i in range(10):
    print("before continue")
    if True:
        continue
    print("silens")


for i in range(21):
    if i % 2 != 0:  # если i не делится без остатка, то if True
        continue  # continue - возвращает нас в начало кода.
    print(f"{i}_even")
"""
3 % 2 = 1
1 != 0
True
trigger continue
нас возвращает в начало

10 % 2 = 0
0 == 0
True
don't trigeer continue
продолжаем идти по коду
"""
