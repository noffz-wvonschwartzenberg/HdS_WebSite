from datetime import datetime
import csv, json
from Mitgliedsantrag.schemas import Mitgliedsantrag, Geschlecht, Abbuchung, Zahlungsweise

def CheckIfAntragIsComplete(antrag: Mitgliedsantrag):
    isAntragFilled = True

    if len(antrag.vorname) == 0:
        isAntragFilled = False
    if len(antrag.nachname) == 0:
        isAntragFilled = False
    if len(antrag.jahresbeitrag) == 0:
        isAntragFilled = False
    if antrag.geschlecht != Geschlecht.MANN and antrag.geschlecht != Geschlecht.FRAU and antrag.geschlecht != Geschlecht.DIVERS:
        isAntragFilled = False
    if len(antrag.strasse) == 0:
        isAntragFilled = False
    if len(antrag.plz) == 0:
        isAntragFilled = False
    if len(antrag.wohnort) == 0:
        isAntragFilled = False
    if len(antrag.geburtsdatum) == 0:
        isAntragFilled = False
    if len(antrag.email) == 0:
        isAntragFilled = False
    if antrag.abbuchung != Abbuchung.SEPA and antrag.abbuchung != Abbuchung.SELBST:
        isAntragFilled = False
    if antrag.abbuchung == Abbuchung.SEPA and len(antrag.kontoinhaber) == 0:
        isAntragFilled = False
    if antrag.abbuchung == Abbuchung.SEPA and len(antrag.iban) == 0:
        isAntragFilled = False
    if antrag.zahlungsweise != Zahlungsweise.JAEHRLICH and antrag.zahlungsweise != Zahlungsweise.HALBJAEHRLICH and antrag.zahlungsweise != Zahlungsweise.VIERTELJAEHRLICH:
        isAntragFilled = False

    return isAntragFilled


def writeAntragCSVfromJSON(antrag: Mitgliedsantrag):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Mitgliedsantrag_{timestamp}.csv"
    
    with open(f".\Antrag\{filename}", mode="w", newline="", encoding="utf-8") as file:
        file.write(f"Vorname: {antrag.vorname}\n")
        file.write(f"Nachname: {antrag.nachname}\n")
        file.write(f"Jahresbeitrag: {antrag.jahresbeitrag}\n")
        file.write(f"Geschlecht: {antrag.geschlecht}\n")
        file.write(f"Strasse: {antrag.strasse}\n")
        file.write(f"PLZ: {antrag.plz}\n")
        file.write(f"Wohnort: {antrag.wohnort}\n")
        file.write(f"Telefonnummer: {antrag.telefonnummer}\n")
        file.write(f"Geburtsdatum: {antrag.geburtsdatum}\n")
        file.write(f"Email: {antrag.email}\n")
        file.write(f"Abbuchung: {antrag.abbuchung}\n")
        file.write(f"Zahlungsweise: {antrag.zahlungsweise}\n")
        file.write(f"Kontoinhaber: {antrag.kontoinhaber}\n")
        file.write(f"IBAN: {antrag.iban}\n")
        file.write(f"BIC: {antrag.bic}\n")
        file.write(f"Zuwendungsbescheinigung: {antrag.zuwendungsbescheinigung}\n")

        
def writeAntragStringfromJSON(antrag: Mitgliedsantrag):
    stringAntrag =  f"Vorname: {antrag.vorname}\n" + \
                    f"Nachname: {antrag.nachname}\n" + \
                    f"Jahresbeitrag: {antrag.jahresbeitrag}\n" + \
                    f"Geschlecht: {antrag.geschlecht}\n" + \
                    f"Strasse: {antrag.strasse}\n" + \
                    f"PLZ: {antrag.plz}\n" + \
                    f"Wohnort: {antrag.wohnort}\n" + \
                    f"Telefonnummer: {antrag.telefonnummer}\n" + \
                    f"Geburtsdatum: {antrag.geburtsdatum}\n" + \
                    f"Email: {antrag.email}\n" + \
                    f"Abbuchung: {antrag.abbuchung}\n" + \
                    f"Zahlungsweise: {antrag.zahlungsweise}\n" + \
                    f"Kontoinhaber: {antrag.kontoinhaber}\n" + \
                    f"IBAN: {antrag.iban}\n" + \
                    f"BIC: {antrag.bic}\n" + \
                    f"Zuwendungsbescheinigung: {antrag.zuwendungsbescheinigung}\n"
    return stringAntrag
        
