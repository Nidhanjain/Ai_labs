# Experiment 10: Simple STRIPS-style Planning
state = {"AtTable", "HandEmpty"}
goal = "Holding"

actions = [
    ("PickUp", {"AtTable", "HandEmpty"}, {"Holding"}, {"AtTable", "HandEmpty"}),
    ("PutDown", {"Holding"}, {"AtTable", "HandEmpty"}, {"Holding"})
]

for name, preconditions, add, delete in actions:
    if preconditions <= state and goal in add:
        print("Plan:", name)
        break
