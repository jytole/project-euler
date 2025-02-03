# Generates a blank tree for problem 018
with open("blank-tree.csv", "a") as f:
    for n in range(120):
        print(["INF"] * 120, file=f)