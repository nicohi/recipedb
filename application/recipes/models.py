from application import db
from application.models import Base

from sqlalchemy.sql import text

recipe_ingredient = db.Table('recipe_ingredient', Base.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'))
)

recipe_tool = db.Table('recipe_tool', Base.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('tool_id', db.Integer, db.ForeignKey('tool.id'))
)

class Recipe(Base):

    __tablename__ = 'recipe'

    name = db.Column(db.String(144), nullable=False)
    favourite = db.Column(db.Boolean, nullable=False)

    ingredients = db.relationship("Ingredient",
                    secondary=recipe_ingredient,
                    backref="recipes")

    tools = db.relationship("Tool",
                    secondary=recipe_tool,
                    backref="recipes")

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    text = db.Column(db.String(), nullable=False)

    def __init__(self, name):
        self.name = name
        self.favourite = False
        self.text = ""

    @staticmethod
    def find_favourites():
        stmt = text("SELECT Recipe.id, Recipe.name FROM Recipe"
                    " WHERE (Recipe.favourite IS 1)")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
