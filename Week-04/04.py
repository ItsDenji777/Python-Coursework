num = int(input("Enter a number: "))
total = 0
k = 1

while k < num :
    if num % k == 0:
        total += k
    k += 1

if total == num:
    print(f"{num} is a Perfect Number!")
else:
    print(f"{num} is NOT a Perfect Number!")