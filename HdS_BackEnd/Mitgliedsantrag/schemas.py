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

class MitgliedsantragBase(BaseModel):
    vorname: str = ""
    nachname: str = ""

class Mitgliedsantrag(MitgliedsantragBase):
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

class MitgliedschaftAdresse(MitgliedsantragBase):
    strasse: str = ""
    plz: str = ""
    wohnort: str = ""
    telefonnummer: str = ""

class MitgliedschaftEmail(MitgliedsantragBase):
    email: str = ""

class MitgliedschaftKonto(MitgliedsantragBase):
    kontoinhaber: str = ""
    iban: str = ""
    bic: str = ""

class MitgliedschaftJahresbeitrag(MitgliedsantragBase):
    jahresbeitrag: str = ""
    abbuchung: Abbuchung = ""
    zahlungsweise: Zahlungsweise = ""
    kontoinhaber: str = ""
    iban: str = ""
    bic: str = ""

class MitgliedschaftZuwendungsbescheinigung(MitgliedsantragBase):
    zuwendungsbescheinigung: Zuwendungsbescheinigung = ""

class MitgliedschaftKuendigen(BaseModel):
    vorname: str = ""
    nachname: str = ""