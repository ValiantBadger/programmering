ord = input ("Skriv här:")

ränkning = {}

for mening in ord:

    if mening.isalpha():

        if mening.lower() in ränkning:
            ränkning[mening.lower()] += 1
        else:

            ränkning[mening.lower()] = 1

for bokstav, antal in ränkning.items():
    print(f"{bokstav} : {antal}")
