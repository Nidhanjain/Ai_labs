# Experiment 15: Rule-Based Medical Expert System
def medical_expert(fever, cough, sore_throat):
    if fever and cough:
        return "Possible flu; consult a doctor"
    if sore_throat:
        return "Possible throat infection; consult a doctor"
    return "Symptoms unclear; consult a doctor if concerned"

print(medical_expert(True, True, False))
