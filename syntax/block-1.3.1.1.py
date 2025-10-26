"""
Условия: if, else, elif.
if_line = input() == "True"
"""

if_line = input("For if_line = ") == "True"
elif_line = input("For elif_line = ") == "True"
if if_line:
    print("stop on if line")
    print(f"because if_line = {if_line}")
elif elif_line:
    print("stop on elif line")
    print(f"because elif_line = {elif_line}")
    print(f"and if_line = {if_line}")
else:
    print("stop on else line,")
    print("because")
    print(f"if_line = {if_line}")
    print(f"elif_line = {elif_line}")
