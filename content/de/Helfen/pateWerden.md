{
    "date": "2025-03-21T19:14:20+01:00",
    "draft": false,
    "title": "Pate werden",
    "author": "WvS",
    "description": "Angelehnt an unser Herzensprojekt \"Eine warme Mahlzeit\" suchen wir Paten, die sich dazu bereit erklären, einem Kind für 1 Jahr eine warme Mahlzeit zu ermöglichen. Bitte helfen Sie einem Kind und werden Pate.",
    "image": "/img/Helfen/PateWerden/PateWerdenTitle.jpeg"
}
## Die Bedeutung einer Patenschaft
DIe Patenschaft ist angelehnt an das Herzensprojekt unseres Vereins "Eine warme Mahlzeit". Wir finden es so wichtig den Kindern eine Grundversorgung zu bieten. Nur so können sie leben und sind in der Lage, eine Schule zu besuchen und sogar einen guten Schulabschluss zu erreichen.  
Das Projekt finanziert sich über die Paten, die den nötigen Beitrag erbringen, damit "ihr" Kind täglich eine warme Mahlzeit erhält.  
Wir sehen aus unserer bereits 7-jährigen Erfahrung, dass die Kinder deutlich gesünder sind und deutlich bessere Noten in der Schule schreiben. Ihr Beitrag als Pate hilft!
  
## Wie stärkt die Patenschaft den Verein
Der Verein wurde gegründet, um den ärmsten Kindern in Mbouda, Kamerun, eine Perspektive zu geben. Sie stärken den Verein durch Ihre Patenschaft, denn Sie unterstützen unser Kernprojekt "Eine warme Mahlzeit". Hier ist der Link zu unserem Projekt: 
<a href="../../Versorgung/EineWarmeMahlzeit">Eine warme Mahlzeit</a> 

## Eine Patenschaft übernehmen
Die rot umrandeten Kinder haben aktuell keinen Paten und würden sich freuen, Sie als Paten zu gewinnen. Bitte wählen Sie ein Patenkind aus.
<div id="kinder-container"></div>

### Die Kosten einer Patenschaft
Die Kosten für eine warme Mahlzeit im Jahr 2018 lagen bei ca. 0,75€ pro Kind pro Tag. 
In den letzten Jahren sind die Preise für Grundnahrungsmittel in Kamerun u. a. durch den Ukrainekrieg aber auch durch den Krieg im eigenen Land stark gestiegen. Die Kosten sind im Jahr 2024 um ca. 60% höher als 2018. Es ergeben sich dadurch Kosten von ca. 1,20€ pro Kind pro Tag.
Durch unser Landwirtschaftsprojekt fließt ein Teil der Erträge direkt in das Projekt “Eine warme Mahlzeit”. Dadurch ist es uns gelungen, den benötigten Betrag pro Kind auf **400€ im Jahr** zu stabilisieren.

### Meine Perönliche Angaben
Geschlecht  
<select id="js-gender" name="gender" required>
    <option value="male">Mann</option>
    <option value="female">Frau</option>
    <option value="diverse">Divers</option>
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
    BIC*  
    <br>
    <input id="js-input-bic" placeholder="">  
</div>
<br>
Die Datenschutzerklärung habe ich gelesen und erkenne Sie ausdrücklich an.  
<br>
<button id="js-button-patenschaft-beantragen">Patenschaft beantragen</button>  
<br>
<div id="message-box" style="display: none;">
    Die Patenschaft wurde beantragt. Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!
    <button id="close-message-btn">Zurück zur Homepage</button>
</div>

<script type="module" src="/js/patenschaft/generateKinderHTML.js"></script>
<script type="module">
    import { generateKinderHTML } from '/js/patenschaft/generateKinderHTML.js';
    document.addEventListener('DOMContentLoaded', () => {
        const container = document.getElementById('kinder-container');
        const showkinderOhnePaten = true;
        const showButton = true;
        const linkedPage = false;
        container.innerHTML = generateKinderHTML(showkinderOhnePaten, showButton, linkedPage);
    });
</script>
<script>
    const selectElement = document.getElementById('js-abbuchung');
    const selectDiv = document.getElementById('js-html-per-SEPA');
    selectElement.addEventListener('change', (event) => {
        const selectedValue = event.target.value;
        if (selectedValue === 'selberUeberweisen') {
            console.log("selber");
            selectDiv.style.display = 'none';
        } else if (selectedValue === 'perSEPA') {
            console.log("sepa");
            selectDiv.style.display = '';
        }
    });
    const selectButton = document.getElementById('js-button-patenschaft-beantragen');
    const messageBox = document.getElementById('message-box');
    const closeMessageBtn = document.getElementById('close-message-btn');
    selectButton.addEventListener('click', () => {
        selectButton.textContent = 'Patenschaft beantragt';
        messageBox.style.display = '';
    });
    closeMessageBtn.addEventListener('click', () => {
        messageBox.style.display = 'none';
        window.location.href = 'https://hdskempen2.netlify.app';
    });
</script>
