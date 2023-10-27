import csv
import statistics
import random
import webbrowser

csv_file = open('sets.csv', newline='')
csv_object = csv.DictReader(csv_file)

release_year: str = input('Podaj rok wydania: ')

element_count = []
images = []

for row in csv_object:
    if row['year'] == release_year:
        element_count.append(int(row['num_parts']))
        images.append(row['img_url'])

print(f'Liczba zestawów wydanych w tym roku to {len(element_count)}!')
print(f'Mediana liczby elementów w zestawie to {statistics.median(element_count)}')
webbrowser.open(random.choice(images))

