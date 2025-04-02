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

<script type="module" src="/js/presse/generatePresseHTML.js"></script>
<script type="module">
    import { generatePresseHTML } from '/js/presse/generatePresseHTML.js';
    document.addEventListener('DOMContentLoaded', () => {
        const container = document.getElementById('article-container');
        container.innerHTML = generatePresseHTML();
    });
</script>
