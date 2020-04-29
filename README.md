# recipedb

A digital cookbook for managing recipes.

[heroku deployment](http://recipedb-nicohi.herokuapp.com/)
```
username: admin
password: admin
```

[user stories](documentation/userstories.md)

[tietokantakaavio](documentation/tables.md)

[features](documentation/features.md)

## Installation instructions

### Setting up venv and installing dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running program
```
python run.py
```

### Updating requirements (devs only)
```
pip freeze | grep -v pkg-resources > requirements.txt
```
