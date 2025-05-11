{
    "date": "2025-03-02T20:26:54+01:00",
    "draft": false,
    "title": "Meine Patenschaft verwalten",
    "author": "WvS",
    "description": "Sie möchten Ihre Patenschaft ändern oder haben Fragen zu Ihrer Patenschaft?",
    "image": "/img/Helfen/PatenschaftVerwalten/PatenschaftVerwaltenTitle.PNG"
}
Bei Anliegen rund um Ihre Patenschaft können Sie uns gerne z. B. per E-Mail kontaktieren.
<input type="checkbox" id="expand-image1" />
<label for="expand-image1">
  <img class="img-centered-half" src="/img/Kontakt.png" alt="Kontakt" />
</label>
<div class="img-caption-half">Kontaktdaten</div>
<br>

## Warum sind Sie Pate?
Sie tragen dazu bei, dass die Kinder in Mbouda, Kamerun, mit Grundnahrungsmitteln versorgt werden. Unsere Kinder erhalten eine Aufgabenbetreuung und werden deutlich besser in der Schule. Bildung ist wichtig!

## Welche Vorteile haben Sie
Sie haben auf jeden Fall den Dank der Kinder und Menschen in Kamerun. Aber Sie bleiben durch Ihre Patenschaft immer informiert. Sie erhalten am Ende jeden Jahres eine Spendenquittung, die Beiträge lassen sich steuerlich absetzen.
<br> 

## Teilen Sie uns Ihre Änderungen mit
<details>
    <summary class="combobox-summary">Änderung der Adresse</summary>
    <div class="combobox-details">
        Bitte geben Sie Ihre neue Adresse ein und senden Sie dann die Daten ab.
        <br><br> 
        Vorname*  
        <input id="js-input-adress-aenderungen-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-adress-aenderungen-nachname" placeholder="" required>  
        <br><br> 
        Straße und Hausnummer*  
        <input id="js-input-adress-aenderungen-strasse" placeholder="" required>  
        <br><br> 
        Postleitzahl*  
        <input id="js-input-adress-aenderungen-plz" placeholder="" required>  
        <br><br> 
        Wohnort*  
        <input id="js-input-adress-aenderungen-wohnort" placeholder="" required>
        <br><br> 
        Telefonnummer  
        <input type="tel" id="js-input-adress-aenderungen-telnummer" placeholder="">  
        <br><br> 
        <button id="js-button-pate-adress-aenderungen">Änderungen abschicken</button>  
        <br><br> 
    </div>
</details>  
<details>
    <summary class="combobox-summary">Änderung der E-Mail Adresse</summary>
    <div class="combobox-details">
        Bitte geben Sie Ihre neue E-Mail Adresse ein und senden Sie dann die Daten ab.
        <br><br> 
        Vorname*  
        <input id="js-input-email-aenderung-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-email-aenderung-nachname" placeholder="" required>  
        <br><br> 
        E-Mail Adresse*  
        <input type="email" id="js-input-email-aenderung-email" placeholder="" required>  
        <br><br> 
        <button id="js-button-pate-email-aenderung">Änderung abschicken</button>  
        <br><br> 
    </div>
</details>
<details>
    <summary class="combobox-summary">Änderung der Kontodaten</summary>
    <div class="combobox-details">  
     Bitte geben Sie Ihre neuen Kontodaten ein und senden Sie dann die Daten ab.
        <br><br> 
        Vorname*  
        <input id="js-input-konto-aenderung-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-konto-aenderung-nachname" placeholder="" required>  
        <br><br> 
        <u>Bankverbindung:</u>
        <br><br> 
        Kontoinhaber*  
        <input id="js-input-konto-aenderung-kontoinhaber" placeholder="">  
        <br><br> 
        IBAN*  
        <br>
        <input id="js-input-konto-aenderung-iban" placeholder="">  
        <br><br> 
        BIC  
        <br>
        <input id="js-input-konto-aenderung-bic" placeholder="">  
        <br><br> 
        Die Datenschutzerklärung habe ich gelesen und erkenne Sie ausdrücklich an.  
        <br>
        <button id="js-button-pate-konto-aenderung">Änderung abschicken</button>  
        <br><br> 
    </div>
</details>
<details>
    <summary class="combobox-summary">Änderung der Beitragshöhe</summary>
    <div class="combobox-details">   
        Bitte geben Sie die neue Jahres-Beitragshöhe in Euro ein und senden Sie dann die Daten ab.  
        <br><br> 
        Vorname*  
        <input id="js-input-jahresbeitrag-aenderung-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-jahresbeitrag-aenderung-nachname" placeholder="" required>  
        <br><br> 
        Tragen Sie nur Zahlen ohne Komma oder Währung ein*  
        <br><br> 
        <input id="js-input-jahresbeitrag-aenderung" placeholder="Jahresbeitrag" required>  
        <br><br> 
        Möchten Sie den Betrag selber überweisen oder sollen wir den Betrag von Ihrem Konto abbuchen?  
        <select id="js-jahresbeitrag-aenderung-abbuchung" name="abbuchung" required>
            <option value="perSEPA">Das Haus der Sonne übernimmt die Abbuchung von Ihrem Konto.</option>
            <option value="selberUeberweisen">Ich überweise den Betrag selbstständig</option>
        </select>
        <div id="js-html-per-SEPA"> 
            <br>
            Bitte buchen Sie den Betrag per SEPA-Lastschriftmandat von meinem nachfolgenden Konto ab.  
            <br>
            Zahlungsweise* 
            <br>
            <select id="js-jahresbeitrag-aenderung-zahlungsweise" name="zahlungsweise" required>
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
            <input id="js-input-jahresbeitrag-aenderung-kontoinhaber" placeholder="">  
            <br>
            IBAN*  
            <br>
            <input id="js-input-jahresbeitrag-aenderung-iban" placeholder="">  
            <br>
            BIC  
            <br>
            <input id="js-input-jahresbeitrag-aenderung-bic" placeholder="">  
        </div>
        <br><br>
        <button id="js-button-pate-jahresbeitrag-aenderung">Änderung abschicken</button>  
        <br><br>   
    </div>
</details>
<details>
    <summary class="combobox-summary">Änderung der Zuwendungsbescheinigung</summary>
    <div class="combobox-details">  
        Bitte tragen Sie Ihre Änderung zur Zuwendungsbescheinigung ein und senden Sie dann die Daten ab.  
        <br><br> 
        Vorname*  
        <input id="js-input-zuwendungsbescheinigung-aenderung-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-zuwendungsbescheinigung-aenderung-nachname" placeholder="" required>  
        <br><br> 
        Bitte wählen Sie, ob Sie eine Zuwendungsbescheinigung für das abgelaufene und gegebenenfalls für die nächsten Jahre erhalten möchten.  
        <br> 
        <select id="js-zuwendungsbescheinigung-aenderung" name="zuwendungsbescheinigung" required>
            <option value="letzteJahr">nur das letzte Jahr</option>
            <option value="diesesJahr">nur dieses Jahr</option>
            <option value="letzteUndNachfolgendeJahre">das letzte Jahr und die nachfolgenden Jahre</option>
        </select>  
        <br><br>
        <button id="js-button-pate-zuwendungsbescheinigung-aenderung">Änderung abschicken</button>  
        <br><br>     
    </div>
</details>
<details>
    <summary class="combobox-summary">Änderung/Beendigung der Patenschaft</summary>
    <div class="combobox-details">
        Wenn Sie Ihre Patenschaft kündigen möchten, bedauern wir das sehr. Wir bedanken uns für Ihren bisherigen Beitrag und wünschen Ihnen alles Gute.
        <br><br> 
        Vorname*  
        <input id="js-input-patenschaft-kuendigen-vorname" placeholder="" required>  
        <br><br> 
        Nachname*  
        <input id="js-input-patenschaft-kuendigen-nachname" placeholder="" required>  
        <br><br>
        <button id="js-button-patenschaft-kuendigen">Patenschaft kündigen</button>  
        <br><br>          
    </div>
</details>
<div id="message-box" style="display: none;">
    <span id="message-box-text">
    Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!</span>
    <button id="close-message-btn">Zurück zur Homepage</button>
</div>
<script>
    const btnAdressAenderung = document.getElementById('js-button-pate-adress-aenderungen');
    const btnEmailAenderung = document.getElementById('js-button-pate-email-aenderung');
    const btnKontoAenderung = document.getElementById('js-button-pate-konto-aenderung');
    const btnJahresbeitragAenderung = document.getElementById('js-button-pate-jahresbeitrag-aenderung');
    const btnZuwendungsbescheinigungAenderung = document.getElementById('js-button-pate-zuwendungsbescheinigung-aenderung');
    const btnPatenschaftKuendigen = document.getElementById('js-button-patenschaft-kuendigen');
    const messageBox = document.getElementById('message-box');
    const messageBoxText = document.getElementById('message-box-text');
    const closeMessageBtn = document.getElementById('close-message-btn');
    btnAdressAenderung.addEventListener('click', () => {
        const vorname = document.getElementById("js-input-adress-aenderungen-vorname").value;
        const nachname = document.getElementById("js-input-adress-aenderungen-nachname").value;
        const strasse = document.getElementById("js-input-adress-aenderungen-strasse").value;
        const plz = document.getElementById("js-input-adress-aenderungen-plz").value;
        const wohnort = document.getElementById("js-input-adress-aenderungen-wohnort").value;
        const telnummer = document.getElementById("js-input-adress-aenderungen-telnummer").value;
        fetch("http://localhost:8000/patenschaftAdressAenderung/", {
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
    btnEmailAenderung.addEventListener('click', () => {
        const vorname = document.getElementById("js-input-email-aenderung-vorname").value;
        const nachname = document.getElementById("js-input-email-aenderung-nachname").value;
        const email = document.getElementById("js-input-email-aenderung-email").value;
        fetch("http://localhost:8000/patenschaftEmailAenderung/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vorname: vorname,
                nachname: nachname,
                email: email,
            })
        })
        .then(async response => {
            const data = await response.json();
            messageBoxText.textContent = data.message
            btnAdressAenderung.textContent = 'Emailänderung beantragt';
            messageBox.style.display = '';
        })
        .catch(error => console.error("Fehler:", error));
    });
    btnKontoAenderung.addEventListener('click', () => {
        const vorname = document.getElementById("js-input-konto-aenderung-vorname").value;
        const nachname = document.getElementById("js-input-konto-aenderung-nachname").value;
        const kontoinhaber = document.getElementById("js-input-konto-aenderung-kontoinhaber").value;
        const iban = document.getElementById("js-input-konto-aenderung-iban").value;
        const bic = document.getElementById("js-input-konto-aenderung-bic").value;
        fetch("http://localhost:8000/patenschaftKontoAenderung/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vorname: vorname,
                nachname: nachname,
                kontoinhaber: kontoinhaber,
                iban: iban,
                bic: bic
            })
        })
        .then(async response => {
            const data = await response.json();
            messageBoxText.textContent = data.message
            btnAdressAenderung.textContent = 'Kontoänderung beantragt';
            messageBox.style.display = '';
        })
        .catch(error => console.error("Fehler:", error));
    });
    btnJahresbeitragAenderung.addEventListener('click', () => {
        const vorname = document.getElementById("js-input-jahresbeitrag-aenderung-vorname").value;
        const nachname = document.getElementById("js-input-jahresbeitrag-aenderung-nachname").value;
        const jahresbeitrag = document.getElementById("js-input-jahresbeitrag-aenderung").value;
        const abbuchung = document.getElementById("js-jahresbeitrag-aenderung-abbuchung").value;
        const zahlungsweise = document.getElementById("js-jahresbeitrag-aenderung-zahlungsweise").value;
        const kontoinhaber = document.getElementById("js-input-jahresbeitrag-aenderung-kontoinhaber").value;
        const iban = document.getElementById("js-input-jahresbeitrag-aenderung-iban").value;
        const bic = document.getElementById("js-input-jahresbeitrag-aenderung-bic").value;
        fetch("http://localhost:8000/patenschaftJahresbeitragAenderung/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vorname: vorname,
                nachname: nachname,
                jahresbeitrag: jahresbeitrag,
                abbuchung: abbuchung,
                zahlungsweise: zahlungsweise,
                kontoinhaber: kontoinhaber,
                iban: iban,
                bic: bic
            })
        })
        .then(async response => {
            const data = await response.json();
            messageBoxText.textContent = data.message
            btnAdressAenderung.textContent = 'Jahresbeitragänderung beantragt';
            messageBox.style.display = '';
        })
        .catch(error => console.error("Fehler:", error));
    });
    btnZuwendungsbescheinigungAenderung.addEventListener('click', () => {
        const vorname = document.getElementById("js-input-zuwendungsbescheinigung-aenderung-vorname").value;
        const nachname = document.getElementById("js-input-zuwendungsbescheinigung-aenderung-nachname").value;
        const zuwendungsbescheinigung = document.getElementById("js-zuwendungsbescheinigung-aenderung").value;
        fetch("http://localhost:8000/patenschaftZuwendungsbescheinigungAenderung/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vorname: vorname,
                nachname: nachname,
                zuwendungsbescheinigung: zuwendungsbescheinigung
            })
        })
        .then(async response => {
            const data = await response.json();
            messageBoxText.textContent = data.message
            btnAdressAenderung.textContent = 'Zuwendungsbescheinigungänderung beantragt';
            messageBox.style.display = '';
        })
        .catch(error => console.error("Fehler:", error));
    });
    btnPatenschaftKuendigen.addEventListener('click', () => {
        const vorname = document.getElementById("js-input-patenschaft-kuendigen-vorname").value;
        const nachname = document.getElementById("js-input-patenschaft-kuendigen-nachname").value;
        fetch("http://localhost:8000/patenschaftKuendigen/", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vorname: vorname,
                nachname: nachname,
            })
        })
        .then(async response => {
            const data = await response.json();
            messageBoxText.textContent = data.message
            btnAdressAenderung.textContent = 'Patenschaft gekündigt';
            messageBox.style.display = '';
        })
        .catch(error => console.error("Fehler:", error));
    });
    closeMessageBtn.addEventListener('click', () => {
        console.log("test");
        messageBox.style.display = 'none';
        window.location.href = 'https://hdskempen2.netlify.app';
    });
</script>
