import random

def del_inn_grupper(deltagere, antall_grupper=None):
    # Hvis antall grupper ikke er gitt, anbefaler vi et antall basert på antall deltagere
    if antall_grupper is None:
        antall_grupper = len(deltagere) // 5  # Anbefaler en gruppe for hver femte deltager

    # Bland deltagerne
    random.shuffle(deltagere)

    # Del deltagerne inn i grupper
    grupper = [deltagere[i::antall_grupper] for i in range(antall_grupper)]

    return grupper

deltagere = ['Mathias', 'Mons', 'Lars', 'Lasse', 'Simon', 'Tobias', 'Isak', 'Daniel', 'Petter', 'Thomas', 'Leander', 'Alf']
antall_grupper = int(input('Hvor mange grupper ønsker du å dele inn i? (la stå tom for anbefaling) ') or 0)

grupper = del_inn_grupper(deltagere, antall_grupper or None)

for i, gruppe in enumerate(grupper, start=1):
    print(f'Gruppe {i}: {", ".join(gruppe)}')