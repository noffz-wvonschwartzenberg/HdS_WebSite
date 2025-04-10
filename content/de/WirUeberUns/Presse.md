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
<!-- <div class="article-line" onclick="window.location.href='https://rp-online.de/nrw/staedte/kempen/kempen-kempener-helfen-kindern-in-kamerun_aid-118664301'">
    <div class="article-column">
        <img src="/img/wirueberuns/presse/Rheinische_Post.png" alt="alt" class="image-logo">
        <p class="article-date">10.10.2010</p>
    </div>
    <p class="article-title">Der Titel</p>
</div> -->
<!-- <a class="article-title" href="${press.ArticleLink}">${press.ArticleTitle}</a> -->


<div id="article-container"></div>

<script type="module" src="/js/presse/generatePresseHTML.js"></script>
<script type="module">
    import { generatePresseHTML } from '/js/presse/generatePresseHTML.js';
    document.addEventListener('DOMContentLoaded', () => {
        const container = document.getElementById('article-container');
        container.innerHTML = generatePresseHTML();
    });
</script>
