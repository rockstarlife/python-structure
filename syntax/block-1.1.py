# make bug 24.10.2025

"""int()"""

bug_1 = int("5 and hellow world")
print(bug_int_but_str)

"""float()"""
bug_2 = float("hellow 2")
print(bug_2)

"""str()"""
bug_3 = str(None)  # str - всеядный, и его не получится забагать.
print(bug_3)

"""bool"""
bug_4 = bool("I'am not a bool")
print(bug_4)
bug_5 = bool()
print(bug_5)
"""Правила:
False: пустые контейнеры, 0, None, False
True: всё остальное"""

"""none()"""

bug_6 = none("is I am real None?")
print(bug_6)
"""none() не существует.
None - это объект-синглтон, а не функция.
Правильно: bug_6 = None
Вызов none() вызовет NameError"""
