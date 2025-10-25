# Здесь будет and, or, not, с цифрами.
a = 3
b = 2
c = 4

num_logic_1 = a + b > c  # True
print(f"a + b > c =  # True {num_logic_1}")
num_logic_2 = (a != b) and not (a == c)  # True
print(f"(a != b) and not (a == c)  # True = {num_logic_2}")
num_logic_3 = (a**2 <= 2 * b + c + 1) or not num_logic_2  # True
print(f"(a**2 <= 2*b+c+1) or not num_logic_2  # True = {num_logic_3}")
num_logic_4 = (a % b == a // b) and not (c % b != 0)  # True
print(f"(a % b == a // b) and not (c % b != 0)  # True = {num_logic_4}")
