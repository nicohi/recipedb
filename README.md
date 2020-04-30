# recipedb

A digital cookbook for managing recipes.

[heroku deployment](http://recipedb-nicohi.herokuapp.com/)
```
username: admin
password: admin
```

[user stories](documentation/userstories.md)

[database information](documentation/tables.md)

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

## Usage instructions
Most functionality is only accessible for logged in users.
So the recommended first step is to register a new user.
Currently all users have the ability to edit all recipes.

After logging in you should be able to navigate all of the pages listed in the top bar.
The titles describe what these pages allow you to do.

### Adding recipe
When adding a new recipe, first create entries for all the ingredients (if they do not already exist).
Then create a recipe entry with a description and navigate to that recipes 'edit' page. (from the recipelist click the recipe, then click 'edit')
Then you can link the ingredients to the recipe with the correct quantities by typing an integer in the text field and pressing '+'.

### Editing a recipe
Navigate to the desired recipe. Press "Edit".
Edit the text and press "Save changes"
Add or remove ingredients with the + and - buttons.

### Searching
Navigate to the "Find recipes" tab.
You can search by entering text into the search field and pressing the button (search looks at all associated text in recipes except ingredients).
You can also add ingredients to filter results. Recipes are sorted by the number of ingredients they use that are in your filter.
