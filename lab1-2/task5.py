import math

a = 3
b = 4
c = 5

# Task 5.
def herons_formula(side_a: float, side_b: float, side_c: float):
    if side_a <= 0 and side_b <= 0 and side_c <= 0:
        return -1
    if side_a > side_b + side_c or side_b > side_a + side_c or side_c > side_a + side_b:
        return -1

    p: float = (side_a + side_b + side_c) / 2
    area: float = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
    return area


def quadratic_equation(a: float, b: float, c: float):
    if a == 0:
        return -1
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return -1
    if delta == 0:
        x = -1 * (b / 2 * a)
        return x
    if delta > 0: # else też by było gitówa
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        return x1, x2


herons_formula(a, b, c)
