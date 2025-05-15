{
    "date": "2025-05-14T21:11:48+01:00",
    "draft": false,
    "title": "Videos",
    "author": "WvS",
    "description": "Hier finden Sie zahlreiche Videos, die das Leben des Vereins widerspiegeln.",
    "image": "/img/Galerie/VideosTitle.jpg"
}

{{< gallery-videos >}}

<script>
document.querySelectorAll('.gallery video').forEach(video => {
    video.onclick = () => {
        document.getElementById('lightbox-video').src = media.src;
        document.getElementById('lightbox-video').style.display = "block";
        document.getElementById('lightbox-video').play();

        document.getElementById('lightbox').style.display = 'flex';
    };
});
</script>