# Hoved funksjonen for min CLI
def calculate() -> float:
    # Her bruker jeg en try-except pga hvis brukeren skriver ikke et tall men f.eks en bokstav får man en ValueError som
    # hadde krasjet programmet
    while True:
        try:
            a = float(input('Skriv inn første tall \n'))
        except ValueError:
            print('Det er ikke et tall, prøv igjen \n')
        else:
            break
    while True:
        try:
            b = float(input('Skriv inn andre tall \n'))
        except ValueError:
            print('Det er ikke et tall, prøv igjen \n')
        else:
            break
    while True:
        op = input('Skriv inn + | - | * | / | % | ** | // \n')
        if op == '+' or op == '-' or op == '*' or op == '/' or op == '%' or op == '**' or op == '//':
            break

    # Her bruker jeg match-case isteded for elif-er pga det er mere optimalisert
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case '%':
            return a % b
        case '**':
            return a ** b
        case '//':
            return a // b
        case _:
            raise Exception


# Her kjører vi funksjonen og printer ut resultatet
print(calculate())
