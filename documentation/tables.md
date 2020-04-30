## Database structure
![tables](tables.png?raw=true)

Recipe_Ingredient and Filter_Ingredient exist to remove many-many relationships between the tables.

## CREATE statements for tables
```
CREATE TABLE recipe_ingredient (
	recipe_id INTEGER, 
	quantity INTEGER, 
	ingredient_id INTEGER, 
	FOREIGN KEY(recipe_id) REFERENCES recipe (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredient (id)
)

CREATE TABLE recipe (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	favourite BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	description VARCHAR NOT NULL, 
	text VARCHAR NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (favourite IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE ingredient (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	unit VARCHAR(144), 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	filter_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(filter_id) REFERENCES filter (id)
)

CREATE TABLE filter_ingredient (
	filter_id INTEGER, 
	ingredient_id INTEGER, 
	FOREIGN KEY(filter_id) REFERENCES filter (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredient (id)
)

CREATE TABLE filter (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
```
