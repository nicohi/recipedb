# recipedb

[heroku-linkki](http://recipedb-nicohi.herokuapp.com/)

## user stories
- Käyttäjä voi tallentaa aineosia, keittiövälineitä ja reseptejä.
- Käyttäjä voi saada ohjelmalta reseptiehdotuksia jollain aineosilla ja keittiövälineillä. Ohjelma valitsee reseptit joihin käyttäjällä on suurin osa aineosista.
- Käyttäjä voi selata ja etsiä reseptejä.

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
