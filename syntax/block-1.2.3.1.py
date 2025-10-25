"""
Логические: and, or, not.
"""

# and
logic_1 = True and True  # True
print(f"True and True = {logic_1}")
logic_2 = True and False  # False
# and подрдазумивает одновременное выполнение всхе элементов.
# один False окрашивает всю строчку в False
print(f"True and False = {logic_2}")
logic_big_1 = False and True and True and True
print(f"False and True and True and True = {logic_big_1}")
# показательный пример. будет False

# or
logic_3 = True or True  # True
print(f"True or True = {logic_3}")
logic_4 = True or False  # True
# Хотя бы один True и вся строчка окрасится в True
print(f"True or False = {logic_4}")
logic_big_2 = True or False or False or False
print(f"True or False or False or False = {logic_big_2}")
# будет True, показательный пример.

# not
logic_5 = not True  # False
print(f"not True = {logic_5}")
logic_6 = not False  # True
print(f"not False = {logic_6}")
# not with and
logic_7 = True and not False and not False  # True
print(f"True and not False and not False = {logic_7}")
logic_8 = not (True and False)  # True
print(f"not (True and False) = {logic_8}")
# not with or
logic_9 = True or not True or not True  # True
print(f"True or not True or not True = {logic_9}")
# and, or, not together
logic_10 = not (True and False) or (True and False)  # True
print(f"not (True and False) or (True and False) = {logic_10}")
logic_11 = not not True  # True
print(f"not not True = {logic_11}")
logic_12 = True and True or False or not True  # True
print(f"True and True or False or not True = {logic_10}")
