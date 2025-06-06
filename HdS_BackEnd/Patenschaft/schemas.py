from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

class Geschlecht(str, Enum):
    MANN = "Mann"
    FRAU = "Frau"
    DIVERS = "Divers"

class Abbuchung(str, Enum):
    SEPA = "perSEPA"
    SELBST = "selberUeberweisen"

class Zahlungsweise(str, Enum):
    JAEHRLICH = "jaehrlich"
    HALBJAEHRLICH = "halbjaehrlich"
    VIERTELJAEHRLICH ="vierteljaehrlich"

class Zuwendungsbescheinigung(str, Enum):
    WIESATZUNG = "wieSatzung"
    LETZTEJAHR = "letzteJahr"
    DIESESJAHR = "diesesJahr"
    LETZTEUNDNACHFOLGENDEJAHRE = "letzteUndNachfolgendeJahre"

class PatenschaftBase(BaseModel):
    vorname: str = ""
    nachname: str = ""

class Patenschaftsantrag(PatenschaftBase):
    kind: str = ""
    jahresbeitrag: str = ""
    geschlecht: Geschlecht = ""
    strasse: str = ""
    plz: str = ""
    wohnort: str = ""
    telefonnummer: str = ""
    geburtsdatum: str = ""
    email: str = ""
    abbuchung: Abbuchung = ""
    zahlungsweise: Zahlungsweise = ""
    kontoinhaber: str = ""
    iban: str = ""
    bic: str = ""
    zuwendungsbescheinigung: Zuwendungsbescheinigung = ""

class PatenschaftAdresse(PatenschaftBase):
    strasse: str = ""
    plz: str = ""
    wohnort: str = ""
    telefonnummer: str = ""

class PatenschaftEmail(PatenschaftBase):
    email: str = ""

class PatenschaftKonto(PatenschaftBase):
    kontoinhaber: str = ""
    iban: str = ""
    bic: str = ""

class PatenschaftJahresbeitrag(PatenschaftBase):
    jahresbeitrag: str = ""
    abbuchung: Abbuchung = ""
    zahlungsweise: Zahlungsweise = ""
    kontoinhaber: str = ""
    iban: str = ""
    bic: str = ""

class PatenschaftZuwendungsbescheinigung(PatenschaftBase):
    zuwendungsbescheinigung: Zuwendungsbescheinigung = ""

class PatenschaftKuendigen(BaseModel):
    vorname: str = ""
    nachname: str = ""