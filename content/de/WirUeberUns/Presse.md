{
    "date": "2025-03-15T21:11:48+01:00",
    "draft": false,
    "title": "Presse",
    "author": "WvS",
    "description": "Eine gute Presse ist wichtig für uns. Der Verein kommt dadurch in alle Munde und viele Menschen lernen uns und unsere Proejkte kennen. Hier geht es zu den bereits veröffentlichten Artikeln.",
    "image": "/img/wirUeberUns/Presse/PresseTitle.png"
}

Bitte informieren Sie sich in der öffentlichen Presse über uns. Hier finden Sie eine Liste der Beiträge.  
<br>
<div id="article-container"></div>

<details>
    <summary class="combobox-summary">
    <p></p>
    <img src="/img/wirUeberUns/Presse/Rheinische_Post.svg" alt="text" class="image-logo" 
    style="width: auto; max-width: 100px; height: auto; max-height: 35px;">
    <p class="article-date" style="font-size: 12px;">Date: 10.1.1000</p>
    Der Traum des Königs der Sonne
    </summary>
    <div class="combobox-details">  
        <iframe src="/img/wirUeberUns/Presse/DerTraumDesKönigsDerSonne.pdf" title="DerTraumDesKönigsDerSonne" width="100%">
        Ihr Browser unterstützt keine PDF-Anzeige.
        </iframe>
    </div>
</details>

<script type="module" src="/js/presse/generatePresseHTML.js"></script>
<script type="module">
    import { generatePresseHTML } from '/js/presse/generatePresseHTML.js';
    document.addEventListener('DOMContentLoaded', () => {
        const container = document.getElementById('article-container');
        container.innerHTML = generatePresseHTML();
    });
</script>
