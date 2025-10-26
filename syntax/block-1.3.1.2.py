"""
Условия: if, else, elif.
С математикой.
"""

x = 5

quest_1 = float(input(f"x = {x}, write x^2 = "))
x_math = x**2
if quest_1 == x_math:
    print("Right.")
elif quest_1 > x_math:
    print(f"less than {quest_1}")
elif quest_1 < x_math:
    print(f"more than {quest_1}")

# print(type(x**2))
# print(type(quest_1))
