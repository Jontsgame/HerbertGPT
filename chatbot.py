# scratch_ai.py

from ai_core import antwort_generieren

print("ScratchAI – Phase 10: SKILLS aktiviert ⚡")
print("Sag Sätze wie: 'starte musik', 'öffne den rechner', 'warum regnet es?'")
print("exit zum Beenden.\n")

while True:
    user_input = input("Du: ")
    if user_input.lower() == "exit":
        break

    antwort = antwort_generieren(user_input)
    print("AI:", antwort)
