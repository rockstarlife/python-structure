"""
break - останавливает цикл при получении
нужного нам условия
"""

for i in range(100):
    print(f"{i}_bef")
    if i == 10:
        print(f"{i}_break\n")
        print(f"Объяснение - мы не дошли до {i}_aft")
        print("потому что был задействован break")
        break
    print(f"{i}_aft\n")


"""
i
0
1
2
3
...
10 break
"""
