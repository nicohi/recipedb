# recipedb

Digitaalinen keittokirja reseptien tallentamiseen ja löytämiseen.

[heroku linkki](http://recipedb-nicohi.herokuapp.com/)


[user stories](documentation/userstories.md)

[tietokantakaavio](documentation/tables.md)

## ohjeita
start venv
```
python3 -m venv venv
source venv/bin/activate
```
install requirements
```
pip install -r requirements.txt
```

run program
```
python run.py
```

update requirements
```
pip freeze | grep -v pkg-resources > requirements.txt
```
