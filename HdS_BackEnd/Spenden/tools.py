from datetime import datetime
import csv, json
from Spenden.schemas import Spendenformular, ProjektAuswahl

def CheckIfSpendenformularIsComplete(antrag: Spendenformular):
    isAntragFilled = True

    if len(antrag.vorname) == 0:
        isAntragFilled = False
    if len(antrag.nachname) == 0:
        isAntragFilled = False
    if antrag.projekt != ProjektAuswahl.ALLGEMEIN and antrag.projekt != ProjektAuswahl.EINEWARMEMAHLZEIT and \
       antrag.projekt != ProjektAuswahl.CAMPUS and antrag.projekt != ProjektAuswahl.SAUBERESWASSER and \
       antrag.projekt != ProjektAuswahl.MEDIZINISCHEVERSORGUNG and antrag.projekt != ProjektAuswahl.GEMUESEGARTEN and \
       antrag.projekt != ProjektAuswahl.NUTZTIERE and antrag.projekt != ProjektAuswahl.UMWELT and \
       antrag.projekt != ProjektAuswahl.WAISENHAEUSER:
        isAntragFilled = False
    if len(antrag.spendenbetrag) == 0:
        isAntragFilled = False
    if len(antrag.strasse) == 0:
        isAntragFilled = False
    if len(antrag.plz) == 0:
        isAntragFilled = False
    if len(antrag.wohnort) == 0:
        isAntragFilled = False
    if len(antrag.email) == 0:
        isAntragFilled = False
    if len(antrag.kontoinhaber) == 0:
        isAntragFilled = False
    if (antrag.iban) == 0:
        isAntragFilled = False

    return isAntragFilled


def writeSpendenformularCSVfromJSON(antrag: Spendenformular):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Spendenformular_{timestamp}.csv"
    
    with open(f".\Antrag\{filename}", mode="w", newline="", encoding="utf-8") as file:
        file.write(f"Vorname: {antrag.vorname}\n")
        file.write(f"Nachname: {antrag.nachname}\n")
        file.write(f"Projekt: {antrag.projekt}\n")
        file.write(f"Spendenbetrag: {antrag.spendenbetrag}\n")
        file.write(f"Strasse: {antrag.strasse}\n")
        file.write(f"PLZ: {antrag.plz}\n")
        file.write(f"Wohnort: {antrag.wohnort}\n")
        file.write(f"Telefonnummer: {antrag.telefonnummer}\n")
        file.write(f"Email: {antrag.email}\n")
        file.write(f"Kontoinhaber: {antrag.kontoinhaber}\n")
        file.write(f"IBAN: {antrag.iban}\n")
        file.write(f"BIC: {antrag.bic}\n")

        
def writeSpendenformularStringfromJSON(antrag: Spendenformular):
    stringAntrag =  f"Vorname: {antrag.vorname}\n" + \
                    f"Nachname: {antrag.nachname}\n" + \
                    f"Projekt: {antrag.projekt}\n" + \
                    f"Spendenbetrag: {antrag.spendenbetrag}\n" + \
                    f"Strasse: {antrag.strasse}\n" + \
                    f"PLZ: {antrag.plz}\n" + \
                    f"Wohnort: {antrag.wohnort}\n" + \
                    f"Telefonnummer: {antrag.telefonnummer}\n" + \
                    f"Email: {antrag.email}\n" + \
                    f"Kontoinhaber: {antrag.kontoinhaber}\n" + \
                    f"IBAN: {antrag.iban}\n" + \
                    f"BIC: {antrag.bic}\n"
    return stringAntrag
        
