# Experiment 8: Predicate Logic
facts = {("Human", "Socrates"), ("Human", "Plato")}

def is_human(name):
    return ("Human", name) in facts

print("Socrates is human:", is_human("Socrates"))
print("Alice is human:", is_human("Alice"))
