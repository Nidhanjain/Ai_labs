# Experiment 2: Simple Reflex Agent - Vacuum Cleaner
def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"

print(vacuum_agent("A", "Dirty"))
print(vacuum_agent("A", "Clean"))
