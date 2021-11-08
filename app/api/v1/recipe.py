from flask import Blueprint, jsonify, request
from ...models import (
    db, Recipe, InstructionInRecipe, IngredientInRecipe, KitchenwareInRecipe
)


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


@bp.route("/api/v1.0.0/public/recipe/recipe_instructions")
def recipe_instructions():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = InstructionInRecipe.query \
        .filter(InstructionInRecipe.recipe_key == key)


    return jsonify(instructions = query.all())



@bp.route("/api/v1.0.0/public/recipe/get_single_recipe_instruction")
def single_recipe_instruction():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = InstructionInRecipe.query \
        .filter(InstructionInRecipe.pk == key)


    return jsonify(instruction = query.first())


@bp.route("/api/v1.0.0/public/recipe/recipe_ingredients")
def recipe_ingredients():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = IngredientInRecipe.query \
        .filter(IngredientInRecipe.recipe_key == key)


    return jsonify(ingredients = query.all())


@bp.route("/api/v1.0.0/public/recipe/get_single_recipe_ingredient")
def single_recipe_ingredient():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = IngredientInRecipe.query \
        .filter(IngredientInRecipe.pk == key)


    return jsonify(ingredient = query.first())


@bp.route("/api/v1.0.0/public/recipe/recipe_kitchenware")
def recipe_kitchenware():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = KitchenwareInRecipe.query \
        .filter(KitchenwareInRecipe.recipe_key == key)


    return jsonify(kitchenware = query.all())


@bp.route("/api/v1.0.0/public/recipe/get_single_recipe_kitchenware")
def single_recipe_kitchenware():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = KitchenwareInRecipe.query \
        .filter(KitchenwareInRecipe.pk == key)


    return jsonify(kitchenware = query.first())
