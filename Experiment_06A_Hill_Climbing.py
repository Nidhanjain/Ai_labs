# Experiment 6A: Hill Climbing
def score(x):
    return -(x - 4) ** 2  # Maximum score occurs at x=4

def hill_climb(x):
    while score(x + 1) > score(x):
        x += 1
    while score(x - 1) > score(x):
        x -= 1
    return x

print("Best position:", hill_climb(0))
print("Best score:", score(hill_climb(0)))
