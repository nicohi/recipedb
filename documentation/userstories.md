# user stories
## As a user I can add and remove recipes
## As a user can edit entries
## As a user can delete entries
## As a user can search for recipes with a string
## As a user I can filter (sorted) search results with ingredients to find recipes that make use of most of the ingredients I have
`FILTER_ID` is the id of the current users filter.
```
SELECT recipe_id FROM recipe_ingredient 
WHERE ingredient_id IN (SELECT ingredient_id FROM filter_ingredient WHERE (filter_id = FILTER_ID)) 
GROUP BY recipe_id 
ORDER BY COUNT(*) DESC;
```
