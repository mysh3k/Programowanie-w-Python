# Task 3.
# Na podstawie tabeli na rok 2023 ze strony (o ile dobrze ją zrozumiałem)
# https://www.pitax.pl/wiedza/poradnik-rozliczenia/progi-podatkowe/
tax_threshold: float = 120000
tax_reducing_amount: float = 3600
choice: int = int(input("""1) Miesięczny
2) Roczny
Wybierz rodzaj dochodu (1-2): """))
income: float = float(input("Podaj dochód (np. 54321.50): "))
if choice == 1:
    income *= 12

if income > tax_threshold:
    tax = 0.32 * (income - tax_threshold) + 10800
else:
    tax = 0.12 * income - tax_reducing_amount

print(tax)