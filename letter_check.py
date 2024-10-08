txt = input('Type your name: ')

print(f'Hello, {txt.capitalize()}!\n')

letter_check = input(f'Is this letter in {txt.capitalize()} : ')

if letter_check not in txt:
    print(f'Ther\'s no {letter_check.upper()} in {txt.capitalize()}!')
else:
    print(f'There\'s {letter_check.upper()} in {txt.capitalize()}!')
