import sys

# En sjekk for om du bruker ihvertfall python 3.6 pga. f-string
MIN_PYTHON = (3, 6)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)


NAME = ['Marcin', 'Rozalski']
AGE = 21

forename = NAME[0]
surname = NAME[1]


# Her bruker jeg en f-string som er en formattert string hvor jeg kan putte variabler i en string (ny i python 3.6)
print(f'Hei. Jeg heter {forename} {surname} og er {AGE} år gammel')