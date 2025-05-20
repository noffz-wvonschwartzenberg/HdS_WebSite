{
    "date": "2025-05-18T11:11:48+01:00",
    "draft": false,
    "title": "Das Vereinsziel",
    "author": "WvS",
    "description": "Das Ziel des Vereins Haus der Sonne.",
    "image": "/img/wirUeberUns/Ziel/ZielTitle.jpg"
}
## Ziel des Vereins Haus der Sonne
Durch unser Bestreben sollen die Kinder und Jugendlichen folgende Ziele erreichen:
- Selbsthilfe und Selbstbestimmung  
Durch unsere Projekte wie z.B. \"Gemüsegarten\" werden die Kinder unterrichtet, wie Gemüse angebaut wird. Daurch lernen sie die Selbstversorgung. 
- Selbstständigkeit  
Gesunde Erwachsene, die sich selbst versorgen können und sogar eine Ausbildung haben, stehen auf eigenen Füßen und brauchen keine weiterer Hilfe mehr.
- Berufswege  
Durch das Erreichen eines schulischen Abschlusses oder sogar einer Ausbildung zeichnen sich für die Kinder und Jugendlichen neu Perspektiven im eigenen Land auf.
- Multiplikatoren  
Durch das Leben als mittelloser Waise und das Erfahren von Hilfe, werden die Kinder nach ihrer Ausbildung zu neuen Ausbildern und so gelingt das Multiplizieren der Hilfe.  

Der Vorstand des Haus der Sonne arbeitet ehrenamtlich für die Unterstützung von Kindern und Jugendlichen, die mittellos oder in auswegloser Lage und auf Hilfe anderer angewiesen sind, in Zusammenarbeit mit unserern Kooperationspartnern vor Ort, wie unserem Parnterverein, Schulen und Ausbildungsstätten.
Im folgenden interaktiven Bild sind unsere Aktivitäten und unser Herzensprojekt dargestellt, den Campus \"Haus der Sonne\" zu bauen.
<br>
<br>
<div class="image-ziel">
    <img src="/img/WirUeberUns/Ziel/Ziel_bild1.png">
  <!-- Brunnen -->
    <div class="hover-area" id="id-hover-area" onclick="showExplanation('Versorgung','/img/WirUeberUns/Ziel/weizen.png','Gesunderhaltung und Brunnen für sauberes Wasser.')" 
         style="top: 150px; left: 170px; width: 80px; height: 110px;">
    </div>
    <!-- Müll -->
    <div class="hover-area" id="id-hover-area" onclick="showExplanation('Versorgung','/img/WirUeberUns/Ziel/weizen.png','Müll/Umwelt Hier ist die Erklärung!\n2. Zeile')" 
         style="top: 255px; left: 60px; width: 90px; height: 100px;">
    </div>
</div>
<br>
<br>
<div class="tabelle-ziel">
    <div class="tabelle-ziel-spalte">
        <h3 class="h3-ziel">Versorgung</h3>
        <img src="/img/WirUeberUns/Ziel/weizen.png" alt="Bild 1">
        <li>Küche/Einrichtung mit einer Tafel für tägliche Mahlzeiten für hilfsbedürftige Kinder und Jugendliche.</li>
        <li>Gesunderhaltung und Brunnen für sauberes Wasser.</li>
        <li>Sicherung der medizinischen Versorgung, Hausapotheke und Erste Hilfe.</li>
    </div>
    <div class="tabelle-ziel-spalte">
        <h3 class="h3-ziel">Überschrift 2</h3>
        <img src="/img/WirUeberUns/Ziel/educationMan.png" alt="Bild 2">
        <li>Küche/Einrichtung mit einer Tafel für tägliche Mahlzeiten für hilfsbedürftige Kinder und Jugendliche.</li>
        <li>Gesunderhaltung und Brunnen für sauberes Wasser.</li>
        <li>Sicherung der medizinischen Versorgung, Hausapotheke und Erste Hilfe.</li>
    </div>
    <div class="tabelle-ziel-spalte">
        <h3 class="h3-ziel">Überschrift 3</h3>
        <img src="/img/WirUeberUns/Ziel/help.png" alt="Bild 3">
        <li>Küche/Einrichtung mit einer Tafel für tägliche Mahlzeiten für hilfsbedürftige Kinder und Jugendliche.</li>
        <li>Küche/Einrichtung mit einer Tafel für tägliche Mahlzeiten für hilfsbedürftige Kinder und Jugendliche.</li>
        <li>Küche/Einrichtung mit einer Tafel für tägliche Mahlzeiten für hilfsbedürftige Kinder und Jugendliche.</li>
    </div>
</div>

## Der Campus \"Haus der Sonne\"
<img class="img-smallest-in-text" src="/img/WirUeberUns/Ziel/campus.png#imagemd" alt="Campus" />
<br>
<br>
Unser großes Herzensprojekt, der Campus \"Haus der Sonne\", wird unser Angebot für die Kinder und Jugendlichen nochmals grundlegend erweitern.  
<br>
<br>
<br>
<ul>
  <li>Es wird ein Waisenhaus für die Kinder und Jugendlichen gebaut.</li>
  <li>Angrenzend bauen wir eine BIldungsstätte mit einer Schule und Ausbildunsmöglichkeiten.</li>
  <li>Für die Versorgung der Anwesenden wird es eine große Kantine geben und eine Brunnen wird auf dem Gelände auch bebohrt.</li>
  <li>Eine Sanitätshaus ist auch geplant.</li>
</ul>

<script>
    function showExplanation(title, img, text) {
        document.querySelectorAll(".explanation-box").forEach(box => box.remove());

        var hoverArea = document.getElementById("id-hover-area");
        let hoverAreaRect = hoverArea.getBoundingClientRect();

        let explanationBox = document.createElement("div");
        explanationBox.className = "explanation-box";

        let heading = document.createElement("h3");
        heading.className = "h3-explanationbox";
        heading.innerText = title;
        explanationBox.appendChild(heading);

        let image = document.createElement("img");
        image.src = img;
        explanationBox.appendChild(image);

        let paragraph = document.createElement("p");
        paragraph.innerText = text;
        explanationBox.appendChild(paragraph);
        
        hoverArea.appendChild(explanationBox);
        explanationBox.style.left = `${event.clientX - hoverAreaRect.left}px`;
        explanationBox.style.top = `${event.clientY - hoverAreaRect.top}px`;
        explanationBox.style.opacity = "1";

        setTimeout(() => explanationBox.remove(), 5000);
    }
</script>