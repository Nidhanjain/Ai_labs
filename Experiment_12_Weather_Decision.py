# Experiment 12: Weather Decision Support
def decision(probability_of_rain):
    if probability_of_rain >= 0.5:
        return "Carry an umbrella"
    return "No umbrella needed"

print(decision(0.7))
