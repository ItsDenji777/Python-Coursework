numbers = []

for i in range(5):
    num = int(input("Input a number: "))
    numbers.append(num)

biggest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > biggest:
        biggest = num

for num in numbers:
    if num < smallest:
        smallest = num

print(f"Biggest number: {biggest}")
print(f"Smallest number: {smallest}")