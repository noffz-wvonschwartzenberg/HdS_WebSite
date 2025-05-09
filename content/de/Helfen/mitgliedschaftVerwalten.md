{
    "date": "2025-03-01T21:11:48+01:00",
    "draft": false,
    "title": "Meine Mitgliedschaft verwalten",
    "author": "WvS",
    "description": "Sie möchten Ihre Mitgliedschaft ändern oder haben Fragen zu Ihrer Mitgliedschaft?",
    "image": "/img/Helfen/MitgliedschaftVerwalten/MitgliedschaftVerwaltenTitle.png"
}
Bei Anliegen rund um Ihre Mitgliedschaft können Sie uns gerne z. B. per E-Mail kontaktieren.
<input type="checkbox" id="expand-image1" />
<label for="expand-image1">
  <img class="img-centered-half" src="/img/Kontakt.png" alt="Kontakt" />
</label>
<div class="img-caption-half">Kontaktdaten</div>
<br>
## Warum sind Sie Mitglied?
Sie tragen dazu bei, dass die Menschen und vor allem die Kinder in Kamerun mit Grundnahrungsmitteln versorgt werden. Unsere Kinder erhalten eine Aufgabenbetreuung und werden deutlich besser in der Schule. Bildung ist wichtig! Durch den Bau zahlreicher Brunnen sind die Menschen plötzlich gesünder.
Durch Ihre Mitgliedschaft unterstützen Sie mit den Verein.
Durch Ihren Beitrag stärken Sie den Verein im allgemeinen, aber Ihr Beitrag wird auch für unsere Projekte dringend benötigt und auch eingesetzt. 

## Welche Vorteile haben Sie
Sie haben auf jeden Fall den Dank der Kinder und Menschen in Kamerun. Aber Sie bleiben durch eine Mitgliedschaft immer informiert. Sie erhalten am Ende jeden Jahres eine Spendenquittung, die Beiträge lassen sich steuerlich absetzen.
<br> 

## Teilen Sie uns Ihre Änderungen mit
<details>
    <summary class="combobox-summary">Änderung der Adresse</summary>
    <div class="combobox-details">
        Bitte geben Sie Ihre neue Adresse ein und senden Sie dann die Daten ab.
        <br><br> 
        Vorname*  
        <input id="js-input-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-nachname" placeholder="" required>  
        <br><br> 
        Straße und Hausnummer*  
        <input id="js-input-strasse" placeholder="" required>  
        <br><br> 
        Postleitzahl*  
        <input id="js-input-plz" placeholder="" required>  
        <br><br> 
        Wohnort*  
        <input id="js-input-wohnort" placeholder="" required>
        <br><br> 
        Telefonnummer  
        <input type="tel" id="js-input-telnummer" placeholder="">  
        <br><br> 
        <button id="js-button-mitglied-adress-aenderungen">Änderungen abschicken</button>  
        <br><br> 
    </div>
</details>  
<details>
    <summary class="combobox-summary">Änderung der E-Mail Adresse</summary>
    <div class="combobox-details">
        Bitte geben Sie Ihre neue E-Mail Adresse ein und senden Sie dann die Daten ab.
        <br><br> 
        Vorname*  
        <input id="js-input-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-nachname" placeholder="" required>  
        <br><br> 
        E-Mail Adresse*  
        <input type="email" id="js-input-email" placeholder="" required>  
        <br><br> 
        <button id="js-button-mitglied-email-aenderung">Änderung abschicken</button>  
        <br><br> 
    </div>
</details>
<details>
    <summary class="combobox-summary">Änderung der Kontodaten</summary>
    <div class="combobox-details">  
     Bitte geben Sie Ihre neuen Kontodaten ein und senden Sie dann die Daten ab.
        <br><br> 
        Vorname*  
        <input id="js-input-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-nachname" placeholder="" required>  
        <br><br> 
        <u>Bankverbindung:</u>
        <br><br> 
        Kontoinhaber*  
        <input id="js-input-kontoinhaber" placeholder="">  
        <br><br> 
        IBAN*  
        <br>
        <input id="js-input-iban" placeholder="">  
        <br><br> 
        BIC  
        <br>
        <input id="js-input-bic" placeholder="">  
        <br><br> 
        Die Datenschutzerklärung habe ich gelesen und erkenne Sie ausdrücklich an.  
        <br>
        <button id="js-button-mitglied-konto-aenderung">Änderung abschicken</button>  
        <br><br> 
    </div>
</details>
<details>
    <summary class="combobox-summary">Änderung der Beitragshöhe</summary>
    <div class="combobox-details">   
        Bitte geben Sie die neue Jahres-Beitragshöhe in Euro ein und senden Sie dann die Daten ab.  
        <br><br> 
        Vorname*  
        <input id="js-input-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-nachname" placeholder="" required>  
        <br><br> 
        Tragen Sie nur Zahlen ohne Komma oder Währung ein*  
        <br><br> 
        <input id="js-input-jahresbeitrag" placeholder="Jahresbeitrag" required>  
        <br><br> 
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
        <br><br>
        <button id="js-button-mitglied-jahresbeitrag-aenderung">Änderung abschicken</button>  
        <br><br>   
    </div>
</details>
<details>
    <summary class="combobox-summary">Änderung der Zuwendungsbescheinigung</summary>
    <div class="combobox-details">  
        Bitte tragen Sie Ihre Änderung zur Zuwendungsbescheinigung ein und senden Sie dann die Daten ab.  
        <br><br> 
        Vorname*  
        <input id="js-input-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-nachname" placeholder="" required>  
        <br><br> 
        Bitte wählen Sie, ob Sie eine Zuwendungsbescheinigung für das abgelaufene und gegebenenfalls für die nächsten Jahre erhalten möchten.  
        <br> 
        <select id="js-zuwendungsbescheinigung" name="zuwendungsbescheinigung" required>
            <option value="letzteJahr">nur das letzte Jahr</option>
            <option value="diesesJahr">nur dieses Jahr</option>
            <option value="letzteUndNachfolgendeJahre">das letzte Jahr und die nachfolgenden Jahre</option>
        </select>  
        <br><br>
        <button id="js-button-mitglied-zuwendungsbescheinigung-aenderung">Änderung abschicken</button>  
        <br><br>     
    </div>
</details>
<details>
    <summary class="combobox-summary">Änderung/Beendigung der Mitgliedschaft</summary>
    <div class="combobox-details">
        Wenn Sie Ihre Mitgliedschaft kündigen möchten, bedauern wir das sehr. Wir bedanken uns für Ihren bisherigen Beitrag und wünschen Ihnen alles Gute.
        <br><br> 
        Vorname*  
        <input id="js-input-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-nachname" placeholder="" required>  
        <br><br>
        <button id="js-button-mitgliedschaft-kuendigen">Mitgliedschaft kündigen</button>  
        <br><br>          
    </div>
</details>
<div id="message-box" style="display: none;">
    <span id="message-box-text">
    Die Mitgliedschaft wurde beantragt. Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!</span>
    <button id="close-message-btn">Zurück zur Homepage</button>
</div>
<script>
    const btnAdressAenderung = document.getElementById('js-button-mitglied-adress-aenderungen');
    const messageBox = document.getElementById('message-box');
    const messageBoxText = document.getElementById('message-box-text');
    const closeMessageBtn = document.getElementById('close-message-btn');
    btnAdressAenderung.addEventListener('click', () => {
        const vorname = document.getElementById("js-input-vorname").value;
        const nachname = document.getElementById("js-input-nachname").value;
        const strasse = document.getElementById("js-input-strasse").value;
        const plz = document.getElementById("js-input-plz").value;
        const wohnort = document.getElementById("js-input-wohnort").value;
        const telnummer = document.getElementById("js-input-telnummer").value;
        fetch("http://localhost:8000/mitgliedschaftAdressAenderung/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vorname: vorname,
                nachname: nachname,
                strasse: strasse,
                plz: plz,
                wohnort: wohnort,
                telefonnummer: telnummer
            })
        })
        .then(async response => {
            const data = await response.json();
            messageBoxText.textContent = data.message
            btnAdressAenderung.textContent = 'Adressänderung beantragt';
            messageBox.style.display = '';
        })
        .catch(error => console.error("Fehler:", error));
    });
    closeMessageBtn.addEventListener('click', () => {
        messageBox.style.display = 'none';
        window.location.href = 'https://hdskempen2.netlify.app';
    });
</script>