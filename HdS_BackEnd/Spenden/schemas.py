from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

class ProjektAuswahl(str, Enum):
    ALLGEMEIN = "allgemein"
    EINEWARMEMAHLZEIT = "eineWarmeMahlzeit"
    CAMPUS = "campus"
    SAUBERESWASSER = "sauberesWasser"
    MEDIZINISCHEVERSORGUNG = "medizinischeVersorgung"
    GEMUESEGARTEN = "gemuesegarten"
    NUTZTIERE = "nutztiere"
    UMWELT = "umwelt"
    WAISENHAEUSER = "waisenhaeuser"

class Spendenformular(BaseModel):
    vorname: str = ""
    nachname: str = ""
    projekt: ProjektAuswahl = ""
    spendenbetrag: str = ""
    strasse: str = ""
    plz: str = ""
    wohnort: str = ""
    telefonnummer: str = ""
    geburtsdatum: str = ""
    email: str = ""
    kontoinhaber: str = ""
    iban: str = ""
    bic: str = ""
