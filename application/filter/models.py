from application import db
from application.models import Base

from sqlalchemy.sql import text

filter_ingredient = db.Table('filter_ingredient', Base.metadata,
    db.Column('filter_id', db.Integer, db.ForeignKey('filter.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'))
)

class Filter(Base):

    __tablename__ = 'filter'

    ingredients = db.relationship("Ingredient",
                    secondary=filter_ingredient,
                    backref="filter")

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, id):
        self.account_id = id

    @staticmethod
    def get_recipes(self):
        stmt = text("SELECT recipe_id FROM recipe_ingredient "
                    "WHERE ingredient_id IN (SELECT ingredient_id FROM filter_ingredient "
                    "WHERE (filter_id = {}))".format(self.id))
        try:
            res = db.engine.execute(stmt)
            response = []
            for row in res:
                response.append(row.values()[0])
            return response
        except:
            return [] 
  
    @staticmethod
    def get_filter(i):

        stmt = text("SELECT id FROM filter "
                    "WHERE (account_id = {})".format(i))
        try:
            res = db.engine.execute(stmt)
            response = []
            for row in res:
                response.append(row.values()[0])
            return response[0]
        except:
            return -1
  
