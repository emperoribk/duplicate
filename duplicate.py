
numbers = list (input('Input your numbers: '))
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

