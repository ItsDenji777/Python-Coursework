# season = input("What season are we in right now? ")

# if season == "Winter":
#     print(f"{season} contains the months: December, January, February")
# elif season == "Autumn":
#     print(f"{season} contains the months: September, October, November")
# elif season == "Spring":
#     print(f"{season} contains the months: March, April, May")
# elif season == "Summer":
#     print(f"{season} contains the months: June, July, August")
# else:
#     print(f"{season} isnt a month!")

# ---------------------------------------------------------------

num = int(input("Enter a number? "))
sum = 0

for i in range(1, num+1):
    sum = sum + i
print(f"The sum of your number with the natural numbers from 1 to {num} is: '{sum}'")