# Task 2.
age: int = int(input("Ile masz lat?: "))
cash: int = int(input("Ile masz pieniędzy w portfelu?: "))

if age >= 18 and cash >= 20:
    print("jesteś pełnoletni i masz wystarczającą ilość pieniędzy")
elif age < 18 and cash >= 20:
    print("nie jesteś pełnoletni i masz wystarczającą ilość pieniędzy")
elif age >= 18 and cash < 20:
    print("jesteś pełnoletni i nie masz wystarczającej ilość pieniędzy")
elif age < 18 and cash < 20:
    print("nie jesteś pełnoletni i nie masz wystarczającej ilość pieniędzy")