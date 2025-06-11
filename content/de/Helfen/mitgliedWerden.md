{
    "date": "2025-03-07T21:11:48+01:00",
    "draft": false,
    "title": "Mitglied werden",
    "author": "WvS",
    "description": "Sie möchten Mitglied im Verein Haus der Sonne werden? Das freut uns sehr.",
    "image": "/img/Helfen/MitgliedWerden/MitgliedWerdenTitle.jpg"
}
## Warum Mitglied werden?
Tragen Sie dazu bei, dass die Menschen und vor allem die Kinder in Kamerun mit Grundnahrungsmitteln versorgt werden. Unsere Kinder erhalten eine Hausaufgabenbetreuung und werden deutlich besser in der Schule. Bildung ist wichtig! Durch den Bau zahlreicher Brunnen sind die Menschen plötzlich gesünder.
Werden Sie Mitglied und unterstützen Sie mit Ihrer Mitgliedschaft den Verein.

### Was macht das Haus der Sonne
- Wir versorgen derzeit bis zu 60 Kindern mit einer täglichen warmen Mahlzeit.
- Bereits 5 Brunnen wurden gebaut.
- Ein Nutztierprojekt ist ins Leben gerufen worden.
- Das Projekt \"Gemüsegarten\" ist ein voller Erfolg.
- viele weitere Projekte und Aktionen für unsere Kinder finden Sie auf unserer Webseite. 

### Wie stärkt meine Mitgliedschaft den Verein
Sie stärken den Verein im allgemeinen, aber Ihr Beitrag wird auch für unsere Projekte dringend benötigt und auch eingesetzt. 

### Welche Vorteile habe ich
Sie haben auf jeden Fall den Dank der Kinder und Menschen in Kamerun. Aber Sie bleiben durch eine Mitgliedschaft immer informiert. Sie erhalten am Ende jeden Jahres eine Spendenquittung, die Beiträge lassen sich steuerlich absetzen.

## Mitgliedschaft beantragen
### Jahresbeitrag in €*
<input id="js-input-jahresbeitrag" placeholder="Jahresbeitrag" required>  

### Persönliche Angaben
Geschlecht  
<select id="js-gender" name="gender" required>
    <option value="Mann">Mann</option>
    <option value="Frau">Frau</option>
    <option value="Divers">Divers</option>
</select>  
  
Vorname*  
<input id="js-input-vorname" placeholder="" required>  
  
Nachname*  
<input id="js-input-nachname" placeholder="" required>  
  
Straße und Hausnummer*  
<input id="js-input-strasse" placeholder="" required>  
  
PLZ*  
<input id="js-input-plz" placeholder="" required>  
  
Wohnort*  
<input id="js-input-wohnort" placeholder="" required>  
  
Telefonnummer  
<input type="tel" id="js-input-telnummer" placeholder="">  

Geburtsdatum* 
<input type="date" id="js-input-geburtsdatum" placeholder="" required>  

E-Mail Adresse*  
<input type="email" id="js-input-email" placeholder="" required>  

### Bezahlung
Möchten Sie den Betrag selber überweisen oder sollen wir den Betrag von Ihrem Konto abbuchen?  
<select id="js-abbuchung" name="abbuchung" required>
    <option value="perSEPA">Das Haus der Sonne übernimmt die Abbuchung von Ihrem Konto.</option>
    <option value="selberUeberweisen">Ich überweise den Betrag selbstständig</option>
</select>
<div id="js-html-per-SEPA"> 
    <br>
    Bitte buchen Sie den Betrag per SEPA-Lastschriftmandat von meinem nachfolgenden Konto ab.  
    <br>
    Zahlungsweise* 
    <br>
    <select id="js-zahlungsweise" name="zahlungsweise" required>
        <option value="jaehrlich">jährlich</option>
        <option value="halbjaehrlich">halbjährlich</option>
        <option value="vierteljaehrlich">vierteljährlich</option>
    </select>  
    <br>
    <br>
    Bankverbindung  
    <br>
    Kontoinhaber*  
    <br>
    <input id="js-input-kontoinhaber" placeholder="">  
    <br>
    IBAN*  
    <br>
    <input id="js-input-iban" placeholder="">  
    <br>
    BIC  
    <br>
    <input id="js-input-bic" placeholder="">  
</div>
<br>
Die Datenschutzerklärung habe ich gelesen und erkenne Sie ausdrücklich an.  
<br>
<button id="js-button-mitglied-werden">Mitgliedsantrag abschicken</button>  
<br>
<div id="message-box" style="display: none;">
    <span id="message-box-text">
    Die Mitgliedschaft wurde beantragt. Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!</span>
    <button id="close-message-btn">Zurück zur Homepage</button>
</div>
<div id="message-box-fehler" style="display: none;">
    <span id="message-box-fehler-text">text</span>
    <button id="close-message-fehler-btn">Ok</button>
</div>

<script>
    const selectElement = document.getElementById('js-abbuchung');
    const selectDiv = document.getElementById('js-html-per-SEPA');
    selectElement.addEventListener('change', (event) => {
        const selectedValue = event.target.value;
        if (selectedValue === 'selberUeberweisen') {
            selectDiv.style.display = 'none';
        } else if (selectedValue === 'perSEPA') {
            selectDiv.style.display = '';
        }
    });
    const selectButton = document.getElementById('js-button-mitglied-werden');
    const messageBox = document.getElementById('message-box');
    const messageBoxText = document.getElementById('message-box-text');
    const messageBoxFehler = document.getElementById('message-box-fehler');
    const messageBoxTextFehler = document.getElementById('message-box-fehler-text');
    const closeMessageBtn = document.getElementById('close-message-btn');
    const closeMessageFehlerBtn = document.getElementById('close-message-fehler-btn');
    selectButton.addEventListener('click', () => {
        const jahresbeitrag = document.getElementById("js-input-jahresbeitrag").value;
        const geschlecht = document.getElementById("js-gender").value;
        const vorname = document.getElementById("js-input-vorname").value;
        const nachname = document.getElementById("js-input-nachname").value;
        const strasse = document.getElementById("js-input-strasse").value;
        const plz = document.getElementById("js-input-plz").value;
        const wohnort = document.getElementById("js-input-wohnort").value;
        const telnummer = document.getElementById("js-input-telnummer").value;
        const geburtsdatum = document.getElementById("js-input-geburtsdatum").value;
        const email = document.getElementById("js-input-email").value;
        const abbuchung = document.getElementById("js-abbuchung").value;
        const zahlungsweise = document.getElementById("js-zahlungsweise").value;
        const kontoinhaber = document.getElementById("js-input-kontoinhaber").value;
        const iban = document.getElementById("js-input-iban").value;
        const bic = document.getElementById("js-input-bic").value;

        fetch("https://hausdersonne-kempen.de/api/mitgliedsantrag/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vorname: vorname,
                nachname: nachname,
                jahresbeitrag: jahresbeitrag,
                geschlecht: geschlecht,
                strasse: strasse,
                plz: plz,
                wohnort: wohnort,
                telefonnummer: telnummer,
                geburtsdatum: geburtsdatum,
                email: email,
                abbuchung: abbuchung,
                zahlungsweise: zahlungsweise,
                kontoinhaber: kontoinhaber,
                iban: iban,
                bic: bic,
                zuwendungsbescheinigung: "wieSatzung"
            })
        })
        .then(async response => {
            const data = await response.json();

            if (!response.ok) {
                messageBoxTextFehler.textContent = data.detail;
                messageBoxFehler.style.display = '';
            } else {
                messageBoxText.textContent = data.message;
                selectButton.textContent = 'Mitgliedschaft beantragt';
                messageBox.style.display = '';
            }
        })
        .catch(error => console.error("Fehler:", error));

    });
    closeMessageBtn.addEventListener('click', () => {
        messageBox.style.display = 'none';
        window.location.href = 'https://hausdersonne-kempen.de';
    });
    closeMessageFehlerBtn.addEventListener('click', () => {
        messageBoxFehler.style.display = 'none';
    });
</script>