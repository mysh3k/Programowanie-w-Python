
# Task 1.
name: str = input("Jak masz na imię?: ")
age: int = int(input("Ile masz lat?: "))

print(f"Cześć {name}!")
print(f"Twoje imię ma {len(name)} liter i zaczyna się od {name[0]}")
print(f"Teraz masz {age} lat, a za rok będzie to {age+1}. Rok urodzenia to {2023-age}")

