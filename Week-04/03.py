num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

prime_numbers = []

for i in range(num1, num2 + 1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
           flag += 1
    if flag == 0 and i > 1:
        prime_numbers.append(i)

print(prime_numbers)