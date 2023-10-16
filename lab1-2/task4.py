
# Task 4.
products: str = input("Wpisz produkty oddzielone przecinkiem (jabłko,banan,ryż,jajka): ")
products_list: list = products.split(',')
products_dict: dict = {}

for product in products_list:
    price: float = float(input(f"Podaj cenę produktu {product}: "))
    products_dict[product] = price

for product, price in products_dict.items():
    print(f"{product}:{price}")
