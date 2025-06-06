from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from tools import sendEmail
from Mitgliedsantrag.schemas import Mitgliedsantrag, \
                                    Zuwendungsbescheinigung as Zuwendungsbescheinigung_Mitgliedschaft, \
                                    MitgliedschaftAdresse, MitgliedschaftEmail, MitgliedschaftKonto, MitgliedschaftJahresbeitrag, MitgliedschaftZuwendungsbescheinigung, MitgliedschaftKuendigen
from Mitgliedsantrag.tools import CheckIfAntragIsComplete as CheckIfMitgliedschaftsAntragIsComplete, \
                                  writeAntragCSVfromJSON as writeMitgliedschaftsAntragCSVfromJSON, \
                                  writeAntragStringfromJSON as writeMitgliedschaftsAntragStringfromJSON
from Patenschaft.schemas import Patenschaftsantrag, \
                                Zuwendungsbescheinigung as Zuwendungsbescheinigung_Patenschaft, \
                                PatenschaftAdresse, PatenschaftEmail, PatenschaftKonto, PatenschaftJahresbeitrag, PatenschaftZuwendungsbescheinigung, PatenschaftKuendigen
from Patenschaft.tools import CheckIfAntragIsComplete as CheckIfPatenschaftsAntragIsComplete, \
                              writeAntragCSVfromJSON as writePatenschaftsAntragCSVfromJSON, \
                              writeAntragStringfromJSON as writePatenschaftsAntragStringfromJSON
from Spenden.schemas import Spendenformular, ProjektAuswahl
from Spenden.tools import CheckIfSpendenformularIsComplete, writeSpendenformularCSVfromJSON, writeSpendenformularStringfromJSON

app = FastAPI()
# ALLOWED_ORIGIN = "localhost:3030"

# # Modell für den Mitgliedsantrag
# class Mitgliedsantrag(BaseModel):
#     geschlecht: str # = Field(..., regex="^(Mann|Frau|Divers)$")
#     vorname: str
#     nachname: str
#     strasse: str
#     plz: str
#     wohnort: str
#     telefonnummer: str
#     geburtsdatum: str
#     email: str
#     zahlungsweise: str
#     kontoinhaber: str
#     iban: str
#     bic: str

# # Zugriffsbeschränkung
# @app.middleware("http")
# async def check_origin(request: Request, call_next):
#     origin = request.headers.get("origin")
#     if origin # and origin != ALLOWED_ORIGIN:
#         raise HTTPException(status_code=403, detail="Zugriff verweigert!")
#     response = await call_next(request)
#     return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Mitgliedsantrag
@app.post("/mitgliedsantrag/", tags=["Mitgliedschaft"])
def empfangen_mitgliedsantrag(antrag: Mitgliedsantrag):
    antrag.zuwendungsbescheinigung = Zuwendungsbescheinigung_Mitgliedschaft.WIESATZUNG
    if CheckIfMitgliedschaftsAntragIsComplete(antrag):
        writeMitgliedschaftsAntragCSVfromJSON(antrag)
        sendEmail("Neuer Mitgliedsantrag", writeMitgliedschaftsAntragStringfromJSON(antrag))
    else:
        raise HTTPException(status_code=400, detail="Der Antrag ist nicht vollständig ausgefüllt")
    
    return {"message": "Der Mitgliedsantrag wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!"}

# Mitgliedschaft verwalten
@app.post("/mitgliedschaftAdressAenderung/", tags=["Mitgliedschaft"])
def empfangen_mitgliedschaftAdressAenderung(adressAenderung: MitgliedschaftAdresse):
    antrag = Mitgliedsantrag(   vorname = adressAenderung.vorname, 
                                nachname = adressAenderung.nachname,
                                strasse = adressAenderung.strasse,
                                plz = adressAenderung.plz,
                                wohnort = adressAenderung.wohnort,
                                telefonnummer = adressAenderung.telefonnummer)
    writeMitgliedschaftsAntragCSVfromJSON(antrag)
    sendEmail("Mitgliedschaft - Adressänderung", writeMitgliedschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Adressänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/mitgliedschaftEmailAenderung/", tags=["Mitgliedschaft"])
def empfangen_mitgliedschaftEmailAenderung(emailAenderung: MitgliedschaftEmail):
    antrag = Mitgliedsantrag(   vorname = emailAenderung.vorname, 
                                nachname = emailAenderung.nachname,
                                email = emailAenderung.email)
    writeMitgliedschaftsAntragCSVfromJSON(antrag)
    sendEmail("Mitgliedschaft - Emailänderung", writeMitgliedschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Emailänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/mitgliedschaftKontoAenderung/", tags=["Mitgliedschaft"])
def empfangen_mitgliedschaftKontoAenderung(kontoAenderung: MitgliedschaftKonto):
    antrag = Mitgliedsantrag(   vorname = kontoAenderung.vorname, 
                                nachname = kontoAenderung.nachname,
                                kontoinhaber = kontoAenderung.kontoinhaber,
                                iban = kontoAenderung.iban,
                                bic = kontoAenderung.bic)
    writeMitgliedschaftsAntragCSVfromJSON(antrag)
    sendEmail("Mitgliedschaft - Kontoänderung", writeMitgliedschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Kontoänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/mitgliedschaftJahresbeitragAenderung/", tags=["Mitgliedschaft"])
def empfangen_mitgliedschaftJahresbeitragAenderung(jahresbeitragAenderung: MitgliedschaftJahresbeitrag):
    antrag = Mitgliedsantrag(   vorname = jahresbeitragAenderung.vorname, 
                                nachname = jahresbeitragAenderung.nachname,
                                jahresbeitrag = jahresbeitragAenderung.jahresbeitrag,
                                abbuchung = jahresbeitragAenderung.abbuchung,
                                zahlungsweise = jahresbeitragAenderung.zahlungsweise,
                                kontoinhaber = jahresbeitragAenderung.kontoinhaber,
                                iban = jahresbeitragAenderung.iban,
                                bic = jahresbeitragAenderung.bic)
    writeMitgliedschaftsAntragCSVfromJSON(antrag)
    sendEmail("Mitgliedschaft - Jahresbeitragänderung", writeMitgliedschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Jahresbeitragänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/mitgliedschaftZuwendungsbescheinigungAenderung/", tags=["Mitgliedschaft"])
def empfangen_mitgliedschaftZuwendungsbescheinigungAenderung(zuwendungsbescheinigungAenderung: MitgliedschaftZuwendungsbescheinigung):
    antrag = Mitgliedsantrag(   vorname = zuwendungsbescheinigungAenderung.vorname, 
                                nachname = zuwendungsbescheinigungAenderung.nachname,
                                zuwendungsbescheinigung = zuwendungsbescheinigungAenderung.zuwendungsbescheinigung)
    writeMitgliedschaftsAntragCSVfromJSON(antrag)
    sendEmail("Mitgliedschaft - Zuwendungsbescheinigungänderung", writeMitgliedschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Zuwendungsbescheinigungänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/mitgliedschaftKuendigen/", tags=["Mitgliedschaft"])
def empfangen_mitgliedschaftKuendigen(mitgliedschaftKuendigen: MitgliedschaftKuendigen):
    antrag = Mitgliedsantrag(   vorname = mitgliedschaftKuendigen.vorname, 
                                nachname = mitgliedschaftKuendigen.nachname)
    writeMitgliedschaftsAntragCSVfromJSON(antrag)
    sendEmail("Mitgliedschaft - Kündigung", writeMitgliedschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Mitgliedschaftkündigung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}


# Patenschaft
@app.post("/patenschaftsantrag/", tags=["Patenschaft"])
def empfangen_patenschaftsantrag(antrag: Patenschaftsantrag):
    antrag.zuwendungsbescheinigung = Zuwendungsbescheinigung_Patenschaft.WIESATZUNG
    if CheckIfPatenschaftsAntragIsComplete(antrag):
        writePatenschaftsAntragCSVfromJSON(antrag)
        sendEmail("Neuer Patenschaftsantrag", writePatenschaftsAntragStringfromJSON(antrag))
    else:
        raise HTTPException(status_code=400, detail="Der Antrag ist nicht vollständig ausgefüllt")
    
    return {"message": "Der Patenschaftsantrag wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!"}


# Patenschaft verwalten
@app.post("/patenschaftAdressAenderung/", tags=["Patenschaft"])
def empfangen_patenschaftAdressAenderung(adressAenderung: PatenschaftAdresse):
    antrag = Patenschaftsantrag(vorname = adressAenderung.vorname, 
                                nachname = adressAenderung.nachname,
                                strasse = adressAenderung.strasse,
                                plz = adressAenderung.plz,
                                wohnort = adressAenderung.wohnort,
                                telefonnummer = adressAenderung.telefonnummer)
    writePatenschaftsAntragCSVfromJSON(antrag)
    sendEmail("Patenschaft - Adressänderung", writePatenschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Adressänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/patenschaftEmailAenderung/", tags=["Patenschaft"])
def empfangen_patenschaftEmailAenderung(emailAenderung: PatenschaftEmail):
    antrag = Patenschaftsantrag(vorname = emailAenderung.vorname, 
                                nachname = emailAenderung.nachname,
                                email = emailAenderung.email)
    writePatenschaftsAntragCSVfromJSON(antrag)
    sendEmail("Patenschaft - Emailänderung", writePatenschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Emailänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/patenschaftKontoAenderung/", tags=["Patenschaft"])
def empfangen_patenschaftKontoAenderung(kontoAenderung: PatenschaftKonto):
    antrag = Patenschaftsantrag(vorname = kontoAenderung.vorname, 
                                nachname = kontoAenderung.nachname,
                                kontoinhaber = kontoAenderung.kontoinhaber,
                                iban = kontoAenderung.iban,
                                bic = kontoAenderung.bic)
    writePatenschaftsAntragCSVfromJSON(antrag)
    sendEmail("Patenschaft - Kontoänderung", writePatenschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Kontoänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/patenschaftJahresbeitragAenderung/", tags=["Patenschaft"])
def empfangen_patenschaftJahresbeitragAenderung(jahresbeitragAenderung: PatenschaftJahresbeitrag):
    antrag = Patenschaftsantrag(vorname = jahresbeitragAenderung.vorname, 
                                nachname = jahresbeitragAenderung.nachname,
                                jahresbeitrag = jahresbeitragAenderung.jahresbeitrag,
                                abbuchung = jahresbeitragAenderung.abbuchung,
                                zahlungsweise = jahresbeitragAenderung.zahlungsweise,
                                kontoinhaber = jahresbeitragAenderung.kontoinhaber,
                                iban = jahresbeitragAenderung.iban,
                                bic = jahresbeitragAenderung.bic)
    writePatenschaftsAntragCSVfromJSON(antrag)
    sendEmail("Patenschaft - Jahresbeitragänderung", writePatenschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Jahresbeitragänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/patenschaftZuwendungsbescheinigungAenderung/", tags=["Patenschaft"])
def empfangen_patenschaftZuwendungsbescheinigungAenderung(zuwendungsbescheinigungAenderung: PatenschaftZuwendungsbescheinigung):
    antrag = Patenschaftsantrag(vorname = zuwendungsbescheinigungAenderung.vorname, 
                                nachname = zuwendungsbescheinigungAenderung.nachname,
                                zuwendungsbescheinigung = zuwendungsbescheinigungAenderung.zuwendungsbescheinigung)
    writePatenschaftsAntragCSVfromJSON(antrag)
    sendEmail("Patenschaft - Zuwendungsbescheinigungänderung", writePatenschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Zuwendungsbescheinigungänderung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}

@app.post("/patenschaftKuendigen/", tags=["Patenschaft"])
def empfangen_patenschaftKuendigen(mitgliedschaftKuendigen: PatenschaftKuendigen):
    antrag = Patenschaftsantrag(vorname = mitgliedschaftKuendigen.vorname, 
                                nachname = mitgliedschaftKuendigen.nachname)
    writePatenschaftsAntragCSVfromJSON(antrag)
    sendEmail("Patenschaft - Kündigung", writePatenschaftsAntragStringfromJSON(antrag))
    
    return {"message": "Die Mitgliedschaftkündigung wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich gegebenenfalls mit Ihnen in Verbindung setzen. Vielen Dank!"}


# Spenden
@app.post("/spenden/", tags=["Spende"])
def empfangen_spenden(antrag: Spendenformular):
    antrag.projekt = ProjektAuswahl.ALLGEMEIN
    if CheckIfSpendenformularIsComplete(antrag):
        writeSpendenformularCSVfromJSON(antrag)
        sendEmail("Neue Spende", writeSpendenformularStringfromJSON(antrag))
    else:
        raise HTTPException(status_code=400, detail="Der Antrag ist nicht vollständig ausgefüllt")
    
    return {"message": "Das Spendenformular wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!"}

# Gezielt Spenden
@app.post("/gezieltSpenden/", tags=["Spende"])
def empfangen_spenden(antrag: Spendenformular):
    if CheckIfSpendenformularIsComplete(antrag):
        writeSpendenformularCSVfromJSON(antrag)
        sendEmail("Neue gezielte Spende", writeSpendenformularStringfromJSON(antrag))
    else:
        raise HTTPException(status_code=400, detail="Der Antrag ist nicht vollständig ausgefüllt")
    
    return {"message": "Das Spendenformular wurde korrekt übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!"}


# # Mitgliedsantrag empfangen und speichern
# @app.get("/")
# async def empfangen_mitgliedsantrag():
#     # # Datei speichern
#     # with open("mitgliedsantrag.txt", "w") as file:
#     #     file.write(antrag.model_dump_json())

#     # # E-Mail versenden
#     # sende_email("Neue Mitgliedsantrag erhalten!")

#     return {"message": "Mitgliedsantrag gespeichert und Benachrichtigung versendet"}

# def sende_email(nachricht):
#     server = smtplib.SMTP("smtp.dein-email-server.de", 587)
#     server.starttls()
#     server.login("deine-email@domain.de", "passwort")
#     server.sendmail("deine-email@domain.de", "ziel-email@domain.de", f"Betreff: Neue Daten\n\n{nachricht}")
#     server.quit()

# # Mitgliedschaftsverwaltung (Beispiel für Änderung der Adresse)
# @app.put("/mitgliedschaft/adresse/")
# async def aendere_adresse(email: str, neue_adresse: str):
#     with open("mitgliedsantrag.txt", "r") as file:
#         lines = file.readlines()
#     updated_lines = [line.replace(f'"email": "{email}"', f'"adresse": "{neue_adresse}"') for line in lines]

#     with open("mitgliedsantrag.txt", "w") as file:
#         file.writelines(updated_lines)

#     return {"message": "Adresse aktualisiert"}

