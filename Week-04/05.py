num = int(input("How many Fibonacci terms do you want? "))
a = 0
b = 1
temp = 0

for i in range(num):
    print(a, end=" ")
    temp = a+b
    a = b
    b = temp