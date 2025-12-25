# Flask (very basic)

Here I have implemented a very basic Flask application keeping the vision of deploying ML models and not by the vision of any front-end (static pages, templates, rendering) or database handling.

To make a curl request:-

1. GET method:-
```curl http://localhost:5000/<further route>``` (may change according to what port is being used)

2. POST method:-
```curl -X POST http://localhost:5000/profile_json -H "Content-Type: application/json" -d '{"name": "XYZ", "rollno": "ABC"}'```
