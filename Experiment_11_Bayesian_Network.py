# Experiment 11: Bayesian Inference
# P(Rain)=0.2, P(Wet|Rain)=0.9, P(Wet|not Rain)=0.1
p_rain = 0.2
p_wet_given_rain = 0.9
p_wet_given_no_rain = 0.1

p_wet = p_rain * p_wet_given_rain + (1 - p_rain) * p_wet_given_no_rain
answer = p_rain * p_wet_given_rain / p_wet
print("Probability of rain given wet grass:", round(answer, 3))
