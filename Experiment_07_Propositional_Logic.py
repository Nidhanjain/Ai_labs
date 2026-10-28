# Experiment 7: Propositional Logic Truth Table
for P in [True, False]:
    for Q in [True, False]:
        print("P =", P, "Q =", Q,
              "AND =", P and Q,
              "OR =", P or Q,
              "P implies Q =", (not P) or Q)
