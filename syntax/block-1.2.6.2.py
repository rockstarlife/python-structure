"""
Площадь крга, равностороннего треугольника, квадрата.
Для равностороннего треугольника:
S = (a * h) / 2
h = √(a² - (a/2)²)
S = √3/4 * a²
"""

a = float(input("Write a = "))
pi = 3.14

s_circle = pi * a**2
print(f"Area of circle with R = a = {a} is {s_circle}")
# h = (a**2 - (a / 2) ** 2) ** (0.5)
# s_triangle = (a * h) / 2
# Не оптимально, зато вывел сам.
s_triangle = 3 ** (0.5) / 4 * a**2
print(f"Area of equilateral triangle is with a = {a} is {s_triangle}")
s_square = a**2
print(f"Area of square with a = {a} is {s_square}")
