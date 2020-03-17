# recipedb

[heroku-linkki](http://recipedb-nicohi.herokuapp.com/)

- ohjelmaan voi tallentaa aineosia, keittiövälineitä ja reseptejä
- ohjelma voi antaa reseptiehdotuksia 

## tietokantataulut (alustava)
![tables](documentation/tables.png?raw=true)


## ohjeita
start venv
```
python3 -m venv venv
source venv/bin/activate
```

update requirements
```
pip freeze | grep -v pkg-resources > requirements.txt
```
