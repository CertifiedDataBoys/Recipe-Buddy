from flask import Blueprint, jsonify, request
from ...models import (
    db,
    Recipe,
    InstructionInRecipe, IngredientInRecipe, KitchenwareInRecipe,
    Ingredient, Kitchenware,
    RecipeComment,
    User
)


bp = Blueprint("api_v1_recipes", __name__)


@bp.route("/api/v1.0.0/public/recipe/get_single_recipe")
def get_single_recipe():
    """
        Create a blueprint to get a single recipe as a JSON file.
        This takes in a recipe's primary key (?pk=<...>).
    """


    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = Recipe.query.filter(Recipe.pk == key)

    return jsonify(recipe = query.first())


@bp.route("/api/v1.0.0/public/recipe/get_single_recipe_details")
def get_single_recipe_details():
    """
        Create a blueprint to get a single recipe's details as a JSON file.
        This takes in a recipe's primary key (?pk=<...>).
    """

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify({"error": True, "message": "No recipe key provided"})


    recipe_details_query = (
        db.session.query(Recipe)
        .join(User, User.uid == Recipe.uploaded_by)
        .with_entities(
            Recipe.title, Recipe.subtitle, Recipe.description, Recipe.uploaded,
            User.uid, User.username
        )
        .filter(Recipe.pk == key)
    )
    recipe_details = recipe_details_query.first()

    # did we get anything?
    if not recipe_details:
        return jsonify({"error": True, "message": "No recipe found"})


    recipe_instructions_query = (
        db.session.query(InstructionInRecipe)
        .with_entities(
            InstructionInRecipe.instruction_number,
            InstructionInRecipe.description, InstructionInRecipe.optional
        )
        .filter(InstructionInRecipe.recipe_key == key)
    )
    recipe_instructions = recipe_instructions_query.all()

    recipe_ingredients_query = (
        db.session.query(IngredientInRecipe)
        .join(Ingredient, Ingredient.pk == IngredientInRecipe.ingredient_key)
        .with_entities(
            IngredientInRecipe.count, IngredientInRecipe.optional,
            Ingredient.name, Ingredient.unit_of_measure,
            Ingredient.units_plural
        )
        .filter(IngredientInRecipe.recipe_key == key)
    )
    recipe_ingredients = recipe_ingredients_query.all()

    recipe_kitchenware_query = (
        db.session.query(KitchenwareInRecipe)
        .join(Kitchenware, Kitchenware.pk == KitchenwareInRecipe.kitchenware_key)
        .with_entities(
            KitchenwareInRecipe.optional,
            Kitchenware.name
        )
        .filter(KitchenwareInRecipe.recipe_key == key)
    )
    recipe_kitchenware = recipe_kitchenware_query.all()

    recipe_comment_query = (
        db.session.query(RecipeComment)
        .join(User, User.uid == RecipeComment.uid)
        .with_entities(
            RecipeComment.contents, RecipeComment.uploaded,
            RecipeComment.suggestion,
            User.uid, User.username
        )
        .filter(RecipeComment.recipe_key == key)
    )
    recipe_comments = recipe_comment_query.all()

    recipe_dict = {
        "title": recipe_details.title,
        "subtitle": recipe_details.subtitle,
        "description": recipe_details.description,
        "uploaded": recipe_details.uploaded,
        "user": {
            "uid" : recipe_details.uid,
            "username": recipe_details.username
        },
        "instructions": sorted([
            {
                "instruction_number": instruction.instruction_number,
                "description": instruction.description,
                "optional": instruction.optional
            }
            for instruction in recipe_instructions
        ], key=lambda col: col["instruction_number"]),
        "ingredients": [
            {
                "count": ingredient.count,
                "optional": ingredient.optional,
                "name": ingredient.name,
                "unit": ingredient.unit_of_measure \
                        if ingredient.count == 1 \
                        else ingredient.units_plural
            }
            for ingredient in recipe_ingredients
        ],
        "kitchenware": [
            {
                "optional": kitchenware.optional,
                "name": kitchenware.name
            }
            for kitchenware in recipe_kitchenware
        ],
        "comments": [
            {
                "contents": comment.contents,
                "uploaded": comment.uploaded,
                "suggestion": comment.suggestion,
                "user":
                {
                    "uid": comment.uid,
                    "username": comment.username
                }
            }
            for comment in recipe_comments
        ]
    }

    return jsonify(recipe=recipe_dict)


@bp.route("/api/v1.0.0/public/recipe/get_recipes")
def get_recipes():
    """
        Create a blueprint to multiple recipes as a JSON file.
        This takes in a recipe's title (?title=<...>) and/or a
        recipe's uploader (uploaded_by=<...>). Note that titles are
        case sensitive and must match a recipe's title completely.<br>

        <b>Examples:</b>

        <tt>/api/v1.0.0/public/recipe/get_recipes?title=Lemon%20Macarons</tt>
        gets all recipes with title="Lemon Macarons"<br>
        <tt>/api/v1.0.0/public/recipe/get_recipes?uploaded_by=1</tt>
        gets all recipes uploaded by the user with uid=1<br>
        <tt>/api/v1.0.0/public/recipe/get_recipes?title=Lemon%20Macarons&uid=1</tt>
        gets all recipes with title="Lemon Macarons" uploaded by the user with
        uid=1.
    """

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
    """
        Create a blueprint to get a single recipe's instructions as a JSON file.
        This takes in a recipe's primary key (?pk=<...>).
    """

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = InstructionInRecipe.query \
        .filter(InstructionInRecipe.recipe_key == key)


    return jsonify(instructions = query.all())



@bp.route("/api/v1.0.0/public/recipe/get_single_recipe_instruction")
def single_recipe_instruction():
    """
        Create a blueprint to get a single instruction a JSON file.
        This takes in an InstructionInRecipe's primary key (?pk=<...>).
    """

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = InstructionInRecipe.query \
        .filter(InstructionInRecipe.pk == key)


    return jsonify(instruction = query.first())


@bp.route("/api/v1.0.0/public/recipe/recipe_ingredients")
def recipe_ingredients():
    """
        Create a blueprint to get a single recipe's ingredients as a JSON file.
        This takes in a recipe's primary key (?pk=<...>).
    """

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = IngredientInRecipe.query \
        .filter(IngredientInRecipe.recipe_key == key)


    return jsonify(ingredients = query.all())


@bp.route("/api/v1.0.0/public/recipe/get_single_recipe_ingredient")
def single_recipe_ingredient():
    """
        Create a blueprint to get a single ingredient a JSON file.
        This takes in an IngredientInRecipe's primary key (?pk=<...>).
    """

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = IngredientInRecipe.query \
        .filter(IngredientInRecipe.pk == key)


    return jsonify(ingredient = query.first())


@bp.route("/api/v1.0.0/public/recipe/recipe_kitchenware")
def recipe_kitchenware():
    """
        Create a blueprint to get a single recipe's kitchenware as a JSON file.
        This takes in a recipe's primary key (?pk=<...>).
    """

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = KitchenwareInRecipe.query \
        .filter(KitchenwareInRecipe.recipe_key == key)


    return jsonify(kitchenware = query.all())


@bp.route("/api/v1.0.0/public/recipe/get_single_recipe_kitchenware")
def single_recipe_kitchenware():
    """
        Create a blueprint to get a single kitchenware item a JSON file.
        This takes in a KitchenwareInRecipe's primary key (?pk=<...>).
    """

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = KitchenwareInRecipe.query \
        .filter(KitchenwareInRecipe.pk == key)


    return jsonify(kitchenware = query.first())
