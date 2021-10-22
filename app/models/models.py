from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Ingredient(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)


class Recipe(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=False, nullable=False)
    uploaded = db.Column(db.DateTime(), unique=False, nullable=False)


class IngredientInRecipe(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    ingredient_key = db.Column(db.Integer, db.ForeignKey("ingredient.pk"),
                               nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                               nullable=False)
    optional = db.Column(db.Boolean, nullable=False)
    count = db.Column(db.Integer, nullable=True)
    unit_of_measure = db.Column(db.String(32), unique=False, nullable=True)
    units_plural = db.Column(db.String(32), unique=False, nullable=True)
