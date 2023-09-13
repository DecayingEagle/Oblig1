# a, b og c skal være konstante og derfor bruker jeg store bokstaver for variable navn
CONST_A = 6
CONST_B = 3
CONST_C = 2

# funksjoner som regner ut resultated
def op_a(a, b, c):
    return a + b * c


def op_b(a, b, c):
    return (a + b) * c


def op_c(a, b, c):
    return a / b / c


def op_d(a, b, c):
    return a / (b / c)

# Her er CLI til dette programmet
while True:
    # Her bruker jeg match-case isteded for elif-er pga det er mere optimalisert
    match input('Velg en \n'
                'a) a + b * c \n'
                'b) (a + b) * c \n'
                'c) a / b / c \n'
                'd) a / (b / c) \n'
                'e) Alle \n'):
        case 'a':
            print('a + b * c = ' + str(op_a(CONST_A, CONST_B, CONST_C)))
            break
        case 'b':
            print('(a + b) * c = ' + str(op_b(CONST_A, CONST_B, CONST_C)))
            break
        case 'c':
            print('a / b / c = ' + str(op_c(CONST_A, CONST_B, CONST_C)))
            break
        case 'd':
            print('a / (b / c) =' + str(op_d(CONST_A, CONST_B, CONST_C)))
            break
        case 'e':
            print('a + b * c = ' + str(op_a(CONST_A, CONST_B, CONST_C)) + '\n')
            print('(a + b) * c = ' + str(op_b(CONST_A, CONST_B, CONST_C)) + '\n')
            print('a / b / c = ' + str(op_c(CONST_A, CONST_B, CONST_C)) + '\n')
            print('a / (b / c) = ' + str(op_d(CONST_A, CONST_B, CONST_C)) + '\n')
            break
        case _:
            print('Prøv igjen \n\n')
