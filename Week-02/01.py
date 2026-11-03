list1 = [1,5,50,3,8,90]
indexed = list1.index(8)
print(f"Before:{list1}")

# list1.pop(indexed)
# list1.insert(indexed, 80)

list1[indexed] = 80

print(f"After:{list1}")