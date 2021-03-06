# user stories
## As a user I can add and remove recipes
Implemented with functions provided by sqlalchemy.
## As a user I can edit entries
Implemented with functions provided by sqlalchemy.
## As a user I can delete entries
Implemented with functions provided by sqlalchemy.
## As a user I can filter (sorted) search results with ingredients to find recipes that make use of most of the ingredients I have
```
SELECT recipe_id FROM recipe_ingredient 
WHERE ingredient_id IN (SELECT ingredient_id FROM filter_ingredient WHERE (filter_id = FILTER_ID)) 
GROUP BY recipe_id 
ORDER BY COUNT(*) DESC;
```
`FILTER_ID` is the id of the current users filter.
This query gets all the recipeIds that use ingredients in the filter. It then sorts them by how many of the filtered ingredients are used in the recipe.
## As a user I can search for recipes with a string
This is done in python by applying a filter to the results of the filtered recipe query.
## As a user I can add and remove ingredients from my filter
A users filter id can be fetched with the following sql query.
```
SELECT id FROM filter
WHERE (account_id = ACCOUNT_ID);
```
`ACCOUNT_ID` is the id of the current user.
The list of ingredients is then modified using sqlalchemy functions.
