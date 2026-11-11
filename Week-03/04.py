colors = ["red", "blue", "aqua", "magenta", "hot pink", "maroon"]
reversed_colors = []

for i in range(len(colors) - 1, -1, -1):
    reversed_colors.append(colors[i])

print(reversed_colors)