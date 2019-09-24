# Calculator

print("Wilkommen zum Rechner-Spiel.")

print("Das sind die Spielregeln: Gib zuerst eine Nummer ein, dann gibt einen Operator ein (+ - / oder *), dann gib die zweite Nummer ein.")

ersteZahl = int(input("Meine erste Zahl lautet: "))

Operator = input("Mein Operator lautet: ")

zweiteZahl = int(input("Meine zweite Zahl lautet: "))

if Operator == "+":
    print(ersteZahl + zweiteZahl)
elif Operator == "-":
    print(ersteZahl - zweiteZahl)
elif Operator == "/":
    print(ersteZahl / zweiteZahl)
elif Operator == "*":
    print(ersteZahl * zweiteZahl)
else:
    print("Sorry, aber deine Eingaben sind nicht gültig.")


