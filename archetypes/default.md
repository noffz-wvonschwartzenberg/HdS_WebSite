{
    "date": "{{ .Date }}",
    "draft": false,
    "title": "{{ replace .File.ContentBaseName "-" " " | title }}",
    "author": "YourName",
    "description": "EnterDescription",
    "image": "img\\folder\\picture.jpg"
}
