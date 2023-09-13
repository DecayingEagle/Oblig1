CAKES_PER_PERSON = [5, 9, 2.5, 21, 0]  # Liste over antallet småkaker per person
amountOfPeople = len(CAKES_PER_PERSON)  # Antall folk

total = sum(CAKES_PER_PERSON)  # Antall total småkaker
print(int(total / amountOfPeople))  # Printer og regner ut gjennomsnittet
