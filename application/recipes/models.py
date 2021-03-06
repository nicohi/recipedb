from application import db
from application.models import Base

from sqlalchemy.sql import text

recipe_ingredient = db.Table('recipe_ingredient', Base.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('quantity', db.Integer),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'))
)

class Recipe(Base):

    __tablename__ = 'recipe'

    name = db.Column(db.String(144), nullable=False)
    favourite = db.Column(db.Boolean, nullable=False)

    ingredients = db.relationship("Ingredient",
                    secondary=recipe_ingredient,
                    backref="recipes")

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    description = db.Column(db.String(), nullable=False)

    text = db.Column(db.String(), nullable=False)

    def __init__(self, name):
        self.name = name
        self.favourite = False
        self.text = ""
        self.description = ""

    @staticmethod
    def get_quantity(self, ingredient_id):
        stmt = text("SELECT quantity FROM recipe_ingredient"
                    " WHERE (recipe_id = {} AND ingredient_id = {})".format(self.id, ingredient_id))
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append(row.values()[0])

        if len(response) is 0:
            return 0
        return response[0]

    @staticmethod
    def set_quantity(self, ingredient_id, quantity):
        stmt = text("UPDATE recipe_ingredient "
                    "SET quantity = {} "
                    "WHERE (ingredient_id = {} AND recipe_id = {})".format(quantity, ingredient_id, self.id))
        res = db.engine.execute(stmt)
        return res

    @staticmethod
    def find_favourites():
        stmt = text("SELECT Recipe.id, Recipe.name FROM Recipe"
                    " WHERE (Recipe.favourite = TRUE)")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
