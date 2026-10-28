# Experiment 9: Forward and Backward Chaining
rules = [({"A"}, "B"), ({"B"}, "C")]

def forward_chaining(facts):
    facts = set(facts)
    changed = True
    while changed:
        changed = False
        for premise, conclusion in rules:
            if premise <= facts and conclusion not in facts:
                facts.add(conclusion)
                changed = True
    return facts

def backward_chaining(goal, facts):
    if goal in facts:
        return True
    for premise, conclusion in rules:
        if conclusion == goal:
            return all(backward_chaining(p, facts) for p in premise)
    return False

print("Forward chaining:", forward_chaining({"A"}))
print("Can prove C:", backward_chaining("C", {"A"}))
print("Resolution example: (P OR Q) and (NOT P) imply Q")
