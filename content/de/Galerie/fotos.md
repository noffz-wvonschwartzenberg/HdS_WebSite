{
    "date": "2025-05-14T21:11:48+01:00",
    "draft": false,
    "title": "Fotos",
    "author": "WvS",
    "description": "Hier finden Sie zahlreiche Bilder, die das Leben des Vereins widerspiegeln.",
    "image": "/img/Galerie/FotosTitle.jpg"
}

{{< gallery-fotos >}}

<script>
document.querySelectorAll('img').forEach(img => {
    img.onload = () => {
        if (img.naturalWidth > img.naturalHeight) {
            img.classList.add("landscape");
            img.classList.remove("portrait");
        } else {
            img.classList.add("portrait");
            img.classList.remove("landscape");
        }
    };
});
document.querySelectorAll('.gallery img').forEach(img => {
    img.onclick = () => {
        document.getElementById('lightbox-img').src = img.src;
        document.getElementById('lightbox').style.display = 'flex';
    };
});
</script>