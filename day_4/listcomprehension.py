number = list(range(10))

evens = [n for n in number if n % 2 == 0 ]
print(evens)

odds = [n for n in number if n % 2 != 0 ]
print(odds)