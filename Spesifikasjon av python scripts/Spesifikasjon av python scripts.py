import pandas as pd
import csv

def generer_brukernavn_epost():
    df = pd.read_excel('C:\\Users\\matrett\\OneDrive - Innlandet fylkeskommune\\2ITK\\Prøveeksamen Mathias\\Spesifikasjon av python scripts\\users.xlsx')
    navn_liste = df['Navn'].tolist()
    brukernavn_epost_liste = [(lag_brukernavn(navn), lag_epost(navn, "@lotus.no")) for navn in navn_liste]
    with open('username_email.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(brukernavn_epost_liste)

def fjern_falske_brukere(brukernavn_liste, nokkelord):
    return [brukernavn for brukernavn in brukernavn_liste if nokkelord not in brukernavn]

def finn_duplikater(deltakerliste):
    frekvens_dict = {}
    for navn in deltakerliste:
        if navn in frekvens_dict:
            frekvens_dict[navn] += 1
        else:
            frekvens_dict[navn] = 1
    return [(navn, frekvens) for navn, frekvens in frekvens_dict.items() if frekvens > 1]

def lag_brukernavn(navn):
    navn_liste = navn.split()
    fornavn = navn_liste[0]
    etternavn = navn_liste[-1]
    brukernavn = (fornavn[:3] + etternavn[0]).lower()
    return brukernavn

def lag_epost(navn, domene):
    brukernavn = lag_brukernavn(navn)
    epost = brukernavn + "@" + domene
    return epost

# Liste med navn
navn = ["Ola", "Kari", "Per", "Nina", "Hans"]
generer_brukernavn_epost()

while True:
    print("\n1) Vis deltakere\n2) Søk etter deltaker\n3) Lag brukernavn\n4) Lag epost\n")
    valg = input("Velg en handling: ")

    if valg == "1":
        # Sorter og vis navnene
        for navn_i in sorted(navn):
            print(navn_i)
    elif valg == "2":
        # Søk etter et navn
        søk_navn = input("Skriv inn navnet du vil søke etter: ")
        if søk_navn in navn:
            print(f"{søk_navn} er i listen.")
        else:
            print(f"{søk_navn} er ikke i listen.")
    elif valg == "3":
        # Lag brukernavn
        navn_input = input("Skriv inn et navn: ")
        print(lag_brukernavn(navn_input))
    elif valg == "4":
        # Lag epost
        navn_input = input("Skriv inn et navn: ")
        domene_input = input("Skriv inn et domene: ")
        print(lag_epost(navn_input, domene_input))
    else:
        print("Ugyldig valg. Prøv igjen.")