numbers = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for n in numbers:
    if n % 3 == 0:
        print(n)

three = [n for n in numbers if n % 3 == 0]
print(three)
