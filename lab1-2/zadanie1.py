import math
# Task 1.
name: str = input("Jak masz na imię?: ")
age: int = int(input("Ile masz lat?: "))

print(f"Cześć {name}!")
print(f"Twoje imię ma {len(name)} liter i zaczyna się od {name[0]}")
print(f"Teraz masz {age} lat, a za rok będzie to {age+1}. Rok urodzenia to {2023-age}")


# Task 2.
cash: int = int(input("Ile masz pieniędzy w portfelu?: "))

if age >= 18 and cash >= 20:
    print("jesteś pełnoletni i masz wystarczającą ilość pieniędzy")
elif age < 18 and cash >= 20:
    print("nie jesteś pełnoletni i masz wystarczającą ilość pieniędzy")
elif age >= 18 and cash < 20:
    print("jesteś pełnoletni i nie masz wystarczającą ilość pieniędzy")
elif age < 18 and cash < 20:
    print("nie jesteś pełnoletni i nie masz wystarczającą ilość pieniędzy")

# Task 3.
# Na podstawie tabeli na rok 2023 ze strony
# https://www.pitax.pl/wiedza/poradnik-rozliczenia/progi-podatkowe/
tax_threshold: float = 120000
tax_reducing_amount: float = 3600
choice: int = int(input("""Wybierz rodzaj dochodu (1-2):
1) Miesięczny
2) Roczny"""))
income: float = float(input("Podaj dochód (np. 54321.50)"))
if choice == 1:
    income *= 12

if income > tax_threshold:
    tax = 0.32 * (income - tax_threshold) + 10800
else:
    tax = 0.12 * income - tax_reducing_amount


# Task 4.
products: str = input("Wpisz produkty oddzielone przecinkiem (jabłko,banan,ryż,jajka): ")
products_list: list = products.split(',')
products_dict: dict = {}

for product in products_list:
    price: float = float(input(f"Podaj cenę produktu {product}: "))
    products_dict[product] = price

for product, price in products_dict.items():
    print(f"{product}:{price}")


# Task 5.
def herons_formula(side_a: float, side_b: float, side_c: float):
    if side_a <= 0 and side_b <= 0 and side_c <= 0:
        return -1
    if side_a > side_b + side_c or side_b > side_a + side_c or side_c > side_a + side_b:
        return -1

    p: float = (side_a + side_b + side_c) / 2
    area: float = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
    return area


def quadratic_equation():
    return

while True:
    try:
        parameters: list = input("Podaj parametry a, b i c oddzielone przecinkiem (3,4,5): ").split(",")
        a, b, c = float(parameters[0]), float(parameters[1]), float(parameters[2])
        print("Pole trójkąta wynosi:", herons_formula(a, b, c))

    except ValueError:
        print("Podaj poprawne wartości")
        continue
