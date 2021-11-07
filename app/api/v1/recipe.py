from flask import Blueprint, jsonify, request
from ...models import db, Recipe


bp = Blueprint("api_v1_recipes", __name__)



@bp.route("/api/v1.0.0/public/recipe/get_single_recipe")
def get_single_recipe():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = Recipe.query.filter(Recipe.pk == key)

    return jsonify(recipe = query.first())


@bp.route("/api/v1.0.0/public/recipe/get_recipes")
def get_recipes():

    title = request.args.get("title")
    uploaded_by = request.args.get("uploaded_by")


    # error handling --- improve later
    if not uploaded_by and not title:

        return jsonify([])


    query = Recipe.query


    if uploaded_by:

        query = query.filter(Recipe.uploaded_by == uploaded_by)

    if title:

        query = query.filter(Recipe.title == title)

    return jsonify(recipes = query.all())
