print('\nVi du vong lap')
languages = ['python <3', 'Java :3', 'Ruby', 'C++', 'C', 'Javascript']

for lang in languages:
    print(lang)

print('\n in vs not in')
print('C#' in languages)
print('C#' not in languages)

print('\nVi du enumerate()')
for index, lang in enumerate(languages):
    print(index, lang)

import random

print('\nrandom.choice()')
print(random.choice(languages))
print('\nrandom.shuffle()')
random.shuffle(languages)
print(languages)

print('\nMethod index()')
index_ex = [1, 2, 3, 4, 3]
print(index_ex.index(2))
print(index_ex.index(3))
# print(index_ex.index(99))

print('\nMethod append() and insert()')
animals = ['dog', 'cat', 'horse']
animals.append('whale')
print(animals)
animals.insert(2, 'lion')
print(animals)

print('\nMethod remove()')
odd_numbers = [1, 3, 5, 7, 9, 3, 3, 3]
odd_numbers.remove(5)
print(odd_numbers)
odd_numbers.remove(3)
print(odd_numbers)

print('\nMethod sort()')
prime_numbers = [4, 7, 5, 7, 9, 7, 6, 4, 3]
prime_numbers.sort()
print(prime_numbers)
prime_numbers.sort(reverse=True)
print(prime_numbers)

print('\nMethod reverse()')
sequence = [1, 2, 3, 4, 5]
sequence.reverse()
print(sequence)
