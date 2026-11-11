number = int(input("Enter a Number: "))
deviders = []
total = 0

for i in range(1, number + 1):
    if number % i == 0:
        deviders.append(i)

for devider in deviders:
    if devider != number:
        total += devider


if total == number:
    print(f"{number} is a Perfect Number!")
else:
    print(f"{number} isn't a Perfect Number.")