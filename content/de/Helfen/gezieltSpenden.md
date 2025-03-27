{
    "date": "2025-03-05T21:11:48+01:00",
    "draft": false,
    "title": "Gezielt spenden",
    "author": "WvS",
    "description": "Spenden Sie gezielt in ein Projekt, wenn Sie sich mit einem unserer Projekt besonders identifizieren können.",
    "image": "/img/Helfen/gezieltSpenden/GezieltSpendenTitle.png"
}
## Wo geht Ihre Spende hin?
Spenden Sie und unterstützen Sie die Kinder und unsere Projekte in Mbouda und Kamerun. Wie in unseren zahlreichen Projekten zu erkennen ist, gehen die Spenden direkt zu den Bedürftigen oder geben Hilfe zur Selbsthilfe, wie z. B. bei dem "Gemüseanbau"-Projekt. Bitte stöbern Sie durch die verschiedenen Bereiche über das was wir tun:
- <a href="../../Versorgung">Auflistung der Projekte zur Versorgung</a>
- <a href="../../HilfeZurSelbsthilfe">Hilfe zur Selbsthilfe</a>
- <a href="../../Bildung">Informationen zu unseren Bildungsprojekten</a>

## Welche Vorteile habe ich
Sie haben auf jeden Fall den Dank der Kinder und Menschen in Kamerun, denn Ihre Spende hilft!
Zu Beginn eines jeden Jahres werden für Spenden im Vorjahr über 100 € Spendenquittungen versandt. Bitte geben Sie zu dem Zweck in der Überweisung Ihre Anschrift an. Auf besonderen Wunsch erhalten Sie auch eine Quittung für eine Spende unter 100 €. Bitte informieren Sie uns in dem Falle per E-Mail: W.v.Schwartzenberg@HausDerSonne-Kempen.de.

## Spenden
### Wählen Sie das Projekt für Ihre Spende aus
Hier finden Sie eine Liste aller Projekte, um Ihre Spende gezielt zu platzieren.  
<!-- <div id="js-projekt-spenden" class="projekt-spenden">
    <ul>
        <li data-value="ein-warme-mahlzeit">Eine warme Mahlzeit</li>
        <li data-value="campus">Campus - Haus der Sonne</li>
        <li data-value="sauberes-wasser">Sauberes Wasser</li>
        <li data-value="medizinische-versorgung">Medizinische Versorgung</li>
        <li data-value="gemuesegarten">Gemüsegarten</li>
        <li data-value="nutztiere">Nutztiere</li>
        <li data-value="umwelt">Umwelt und Müll</li>
        <li data-value="waisenhaeuser">Waisenhäuser</li>
    </ul>
</div> -->
<select id="js-projekt-spenden" name="ProjektSpenden" required>
    <option value="ein-warme-mahlzeit">Eine warme Mahlzeit</option>
    <option value="campus">Campus - Haus der Sonne</option>
    <option value="sauberes-wasser">Sauberes Wasser</option>
    <option value="medizinische-versorgung">Medizinische Versorgung</option>
    <option value="gemuesegarten">Gemüsegarten</option>
    <option value="nutztiere">Nutztiere</option>
    <option value="umwelt">Umwelt und Müll</option>
    <option value="waisenhaeuser">Waisenhäuser</option>
</select>  

### Wie möchten Sie spenden
<details>
    <summary class="combobox-summary">Spendenkonto</summary>
    <div class="combobox-details">
        Überweisen Sie selbstständig einen Betrag auf unser Spendenkonto. Bitte tragen Sie Ihren Namen und Ihre Adresse in den Verwendungszweck ein, damit wir Ihnen gegebenenfalls eine Spendenquittung zusenden können.  
        Und vergessen Sie nicht das Projekt im Verwendungszweck mit anzugeben.
        <br>
        <input type="checkbox" id="expand-image1" />
        <label for="expand-image1">
        <img class="img-centered-half" src="/img/Spendenkonto.png" alt="Spendenkonto" />
        </label>
        <div class="img-caption-half">Spendenkonto</div>
        <br>    
    </div>
</details>
<details>
    <summary class="combobox-summary">Paypal</summary>
    <div class="combobox-details">
        Spenden Sie auf die einfachste Art und Weise, mit Paypal.  
        Schreiben Sie uns gegebenenfalls eine kurze E-Mail, mit dem Hinweis Ihrer Spende und dem Projekt, das Sie erreichen wollen.
        <div class="div-donate-paypal">
            <!-- <button>Direkt über Paypal spenden</button> -->
            <form action="https://www.paypal.com/donate" method="post" target="_top">
                <input class="donate-paypal-hosted" type="hidden" name="hosted_button_id" value="JVEF3JGFNK2ML" />
                <input class="donate-paypal-image" type="image" src="https://www.paypalobjects.com/de_DE/DE/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Spenden mit dem PayPal-Button" />
                <img class="donate-paypal-img" alt="" border="0" src="https://www.paypal.com/de_DE/i/scr/pixel.gif" width="1" height="1" />
            </form>
        </div>   
    </div>
</details>
<details>
    <summary class="combobox-summary">Online-Spende</summary>
    <div class="combobox-details">
        Die Online-Spende ist für Sie eine angenehme Art der Spende. Sie teilen uns Ihre Angaben und den gewünschten Betrag mit und wir kümmern uns um den Rest. Wir weisen den Betrag dem ausgewählten Projekt zu.
        <br>
        <br>
        Spendenbetrag in Euro*  
        <input id="js-input-spendenbeitrag" placeholder="Spendenbetrag" required>  
        <br>
        Vorname*  
        <input id="js-input-vorname" placeholder="" required>  
        <br>
        Nachname*  
        <input id="js-input-nachname" placeholder="" required>  
        <br>
        Straße und Hausnummer*  
        <input id="js-input-strasse" placeholder="" required>  
        <br>
        PLZ*  
        <br>
        <input id="js-input-plz" placeholder="" required>  
        <br>
        Wohnort*  
        <input id="js-input-wohnort" placeholder="" required>  
        <br>
        Telefonnummer  
        <input type="tel" id="js-input-telnummer" placeholder="">  
        <br>
        E-Mail Adresse  
        <input type="email" id="js-input-email" placeholder="" required>  
        <br>
        <div id="js-html-per-SEPA"> 
            <br>
            Bitte buchen Sie den Betrag per SEPA-Lastschriftmandat von meinem nachfolgenden Konto ab:  
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
        <button id="js-button-spenden">Spende auslösen</button>  
        <br>
        <br>
        <div id="message-box" style="display: none;">
            Die Angaben für Ihre Spende wurde übertragen. Das Haus der Sonne überprüft Ihre Angaben und wird sich so schnell wie möglich mit Ihnen in Verbindung setzen. Vielen Dank!
            <button id="close-message-btn">Zurück zur Homepage</button>
        </div>      
    </div>
</details>
  
### Wollen Sie langfristig spenden?
Wenn Sie uns lieber langfristig unterstützen möchten, bieten wir Ihnen die Möglichkeit eine Patenschaft zu übernehmen oder auch eine Mitgliedschaft abzuschließen. Sie können den Betrag dann ganz einfach per Lastschrift von uns abbuchen lassen. Besuchen Sie die entsprechenden Seiten, um sich noch genauer zu informieren:
- <a href="../pateWerden">Informationen zur Patenschaft</a>
- <a href="../mitgliedWerden">Informationen zur Mitgliedschaft</a>
