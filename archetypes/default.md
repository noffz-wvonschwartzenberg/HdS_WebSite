{
    "date": "{{ .Date }}",
    "draft": true,
    "title": "{{ replace .File.ContentBaseName "-" " " | title }}",
    "author": "YourName",
    "description": "EnterDescription",
    "image": "img\\folder\\picture.jpg"
}
