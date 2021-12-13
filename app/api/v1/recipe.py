from datetime import datetime
from flask import Blueprint, jsonify, request
from ...models import (
    db,
    Recipe,
    InstructionInRecipe, IngredientInRecipe, KitchenwareInRecipe, MediaInRecipe,
    Ingredient, Kitchenware,
    RecipeComment,
    DietaryRestriction, RestrictionOnIngredient,
    User
)
from sqlalchemy.sql import func
from flask_login import current_user

bp = Blueprint("api_v1_recipes", __name__)


@bp.route("/api/v1.0.0./public/recipe/get_random", methods=["GET"])
def get_random():
    """
    Get multiple random recipes
    """

    quantity = request.args.get("quantity", default=10, type=int)
    typeFilter = request.args.get("typeFilter", type=str)
    kitchenwareFilter = request.args.get("kitchenwareFilter", type=str)

    if request.method == "GET":
        try:
            if not typeFilter and not kitchenwareFilter:
                recipes = Recipe.query \
                    .order_by(func.rand()) \
                    .filter(Recipe.is_private == False) \
                    .limit(quantity) \
                    .all()
            elif typeFilter and not kitchenwareFilter:
                recipes = Recipe.query \
                    .filter(Recipe.is_private == False and Recipe.type == typeFilter) \
                    .order_by(func.rand()) \
                    .limit(quantity) \
                    .all()
            elif not typeFilter and kitchenwareFilter:
                #if "," in typeFilter:
                #    typeFilterArr = typeFilter.split(",")
                #    recipes = Recipe.query.filter(Recipe.kitchenware.any(Kitchenware.name.in_(typeFilter))).order_by(func.rand()).limit(quantity).all()
                #else:
                #    recipes = Recipe.query.filter_by(Recipe.kitchenware.any(Kitchenware.name == kitchenwareFilter)).order_by(func.rand()).limit(quantity).all()
                recipes = {}
            else:
                recipes = {}
            return jsonify({"recipes": recipes})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


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

    # are we allowed to view this recipe?
    if not user_can_view_recipe(key):

        return jsonify([])

    query = Recipe.query.filter(Recipe.pk == key)

    return jsonify(recipe=query.first())


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

    # are we allowed to view this recipe?
    if not user_can_view_recipe(key):

        return jsonify([])

    recipe_details_query = (
        db.session.query(Recipe)
        .join(User, User.uid == Recipe.uploaded_by)
        .with_entities(
            Recipe.title, Recipe.subtitle, Recipe.description, Recipe.uploaded,
            Recipe.type, Recipe.is_private,
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
            RecipeComment.pk, RecipeComment.contents, RecipeComment.uploaded,
            RecipeComment.reply_to, RecipeComment.suggestion,
            User.uid, User.username
        )
        .filter(RecipeComment.recipe_key == key)
    )
    recipe_comments = recipe_comment_query.all()

    recipe_media_query = (
        db.session.query(MediaInRecipe)
        .join(Recipe, Recipe.pk == MediaInRecipe.recipe_key)
        .with_entities(
            MediaInRecipe.pk, MediaInRecipe.media_link, MediaInRecipe.is_video
        )
        .filter(MediaInRecipe.recipe_key == key)
    )
    recipe_media = recipe_media_query.all()

    recipe_dict = {
        "title": recipe_details.title,
        "subtitle": recipe_details.subtitle,
        "description": recipe_details.description,
        "uploaded": recipe_details.uploaded,
        "type": recipe_details.type,
        "is_private": recipe_details.is_private,
        "user": {
            "uid": recipe_details.uid,
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
                "unit": ingredient.unit_of_measure
                if ingredient.count == 1
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
                "pk": comment.pk,
                "contents": comment.contents,
                "uploaded": comment.uploaded,
                "reply_to": comment.reply_to,
                "suggestion": comment.suggestion,
                "user":
                {
                    "uid": comment.uid,
                    "username": comment.username
                }
            }
            for comment in recipe_comments
        ],
        "media": [
            {
                "pk": media.pk,
                "media_link": media.media_link,
                "is_video": media.is_video
            }
            for media in recipe_media
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

    # are we allowed to view this recipe?
    if not user_can_view_recipe(key):

        return jsonify([])

    query = Recipe.query

    if uploaded_by:

        query = query.filter(Recipe.uploaded_by == uploaded_by)

    if title:

        query = query.filter(Recipe.title == title)

    return jsonify(recipes=query.all())


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

    # are we allowed to view this recipe?
    if not user_can_view_recipe(key):

        return jsonify([])

    query = InstructionInRecipe.query \
        .filter(InstructionInRecipe.recipe_key == key)

    return jsonify(instructions=query.all())


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

    # are we allowed to view this recipe?
    if not user_can_view_recipe(key):

        return jsonify([])

    query = InstructionInRecipe.query \
        .filter(InstructionInRecipe.pk == key)


    return jsonify(instruction=query.first())


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

    # are we allowed to view this recipe?
    if not user_can_view_recipe(key):

        return jsonify([])

    query = IngredientInRecipe.query \
        .filter(IngredientInRecipe.recipe_key == key)

    return jsonify(ingredients=query.all())


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

    return jsonify(ingredient=query.first())


@bp.route("/api/v1.0.0/public/recipe/get_recipe_restrictions")
def get_recipe_restrictions():
    """
        Using a recipe's ingredients, fetch all of the restrictions this
        recipe complies with.
    """

    key = request.args.get("pk")

    # error handling --- improve later
    if not key:

        return jsonify([])

    # are we allowed to view this recipe?
    if not user_can_view_recipe(key):

        return jsonify([])

    ingredients_count = IngredientInRecipe.query \
        .filter(IngredientInRecipe.recipe_key == key) \
        .filter(IngredientInRecipe.optional == False) \
        .with_entities(func.count(IngredientInRecipe.pk)) \
        .scalar()

    ingredients_query = Ingredient.query \
        .join(IngredientInRecipe, IngredientInRecipe.recipe_key == key) \
        .filter(IngredientInRecipe.ingredient_key == Ingredient.pk) \
        .filter(IngredientInRecipe.optional == False) \
        .with_entities(Ingredient.pk)

    restrictions_count = dict()

    for ingredient in ingredients_query.all():

        restrictions_on_ingredient = RestrictionOnIngredient.query \
            .filter(RestrictionOnIngredient.ingredient_key == ingredient.pk) \
            .with_entities(RestrictionOnIngredient.restriction_key)

        for restriction in restrictions_on_ingredient.all():

            restriction_key = restriction.restriction_key

            if restriction_key in restrictions_count:
                restrictions_count[restriction_key] += 1
            else:
                restrictions_count[restriction_key] = 1

    # Build a list of all restrictions where each restriction is used by every
    # single non-optional ingredient
    restrictions_list = [
                            restriction for restriction in restrictions_count
                            if restrictions_count[restriction] == ingredients_count
                        ]

    return jsonify(restrictions=restrictions_list)


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

    # are we allowed to view this recipe?
    if not user_can_view_recipe(key):

        return jsonify([])

    query = KitchenwareInRecipe.query \
        .filter(KitchenwareInRecipe.recipe_key == key)

    return jsonify(kitchenware=query.all())


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

    return jsonify(kitchenware=query.first())


@bp.route("/api/v1.0.0/public/recipe/search_recipes")
def search_recipes():
    """
        Create a blueprint to search for recipes as a JSON file.
    """
    query = request.args.get("q")

    if not query:
        return jsonify([])
    else:
        # limit of 512 characters per search query
        queries = query[:512].lower().split("||")
        # sanitize input
        queries = [term.replace("%","").replace("_","") for term in queries]
        # recipes_query = db.session.query(Recipe)
        term_queries = [ ]
        results = dict()

        for term in queries:

            this_query = db.session.query(Recipe)

            for t in term.split("&&"):

                full_search_term = "%" + t.strip() + "%"
                # split on the first ":"
                current_search = t.lower().split(":", 1)

                # Was a colon found?
                if len(current_search) == 2:

                    search_category = current_search[0]
                    search_string = "%" + current_search[1].strip() + "%"
                    # What are we searching for?
                    if search_category == "title":
                        this_query = this_query.filter(Recipe.title.like(search_string))
                    elif search_category == "subtitle":
                        this_query = this_query.filter(Recipe.subtitle.like(search_string))
                    elif search_category == "description":
                        this_query = this_query.filter(Recipe.description.like(search_string))
                    elif search_category == "type":
                        this_query = this_query.filter(Recipe.type.like(search_string))
                    # This category doesn't exist!
                    else:
                        this_query = this_query.filter(
                            Recipe.title.like(full_search_term)
                            | Recipe.subtitle.like(full_search_term)
                            | Recipe.description.like(full_search_term)
                            | Recipe.type.like(full_search_term)
                        )


                    term_queries.append(this_query)

                # No colon found. . .
                else:
                    # If no search term was given, skip! Otherwise . . .
                    if full_search_term != "%%":
                        this_query = this_query.filter(
                            Recipe.title.like(full_search_term)
                            | Recipe.subtitle.like(full_search_term)
                            | Recipe.description.like(full_search_term)
                            | Recipe.type.like(full_search_term)
                        )
                        term_queries.append(this_query)


        for tq in term_queries:

            for recipe in tq:

                # are we allowed to view this recipe?
                if not user_can_view_recipe(recipe.pk):

                    continue

                if not recipe.pk in results:

                    results[recipe.pk] = {"recipe": recipe, "score": 1}

                else:

                    results[recipe.pk]["score"] += 1

        return jsonify(recipes=results)


@bp.route("/api/v1.0.0/public/recipe/upload_recipe", methods=['GET', 'POST'])
def upload_recipe():
    # Is this user not logged in?
    if not current_user.is_authenticated:
        return jsonify(recipe=[])

    if request.method == "POST":

        uid = current_user.get_id()

        # No recipe data uploaded
        if "recipe" not in request.json:

            return jsonify(recipe={
                "uid": uid,
                "pk": -1,
                "upload_successful": False
            })

        new_recipe = Recipe(title=request.json["recipe"]["title"],
                            subtitle=request.json["recipe"]["subtitle"],
                            description=request.json["recipe"]["description"],
                            type=request.json["recipe"]["type"],
                            uploaded=datetime.now(),
                            uploaded_by=uid,
                            is_private=request.json["recipe"]["is_private"])

        db.session.add(new_recipe)
        db.session.commit()

        for ingredient in request.json["recipe"]["ingredients"]:
            # Check to see if ingredient already exists in database
            ingredient_in_db = Ingredient.query.filter(
                Ingredient.name == ingredient["name"], Ingredient.unit_of_measure == ingredient["units"]).first()
            if ingredient_in_db:
                ingredient["ingredient_key"] = ingredient_in_db.pk
            else:
                if int(ingredient["count"]) > 1:
                    new_ingredient = Ingredient(
                        name=ingredient["name"], units_plural=ingredient["units"])
                else:
                    new_ingredient = Ingredient(
                        name=ingredient["name"], unit_of_measure=ingredient["units"])
                db.session.add(new_ingredient)
                db.session.commit()
                ingredient["ingredient_key"] = new_ingredient.pk

        new_ingredients = [
            IngredientInRecipe(
                ingredient_key=ingredient["ingredient_key"],
                recipe_key=new_recipe.pk,
                optional=ingredient["optional"],
                count=ingredient["count"]
            )
            for ingredient in request.json["recipe"]["ingredients"]
        ]
        new_instructions = [
            InstructionInRecipe(
                recipe_key=new_recipe.pk,
                description=instruction["description"],
                instruction_number=instruction["instruction_number"],
                optional=instruction["optional"]
            )
            for instruction in request.json["recipe"]["instructions"]
        ]
        new_media = [
            MediaInRecipe(
                recipe_key=new_recipe.pk,
                media_link=media["media_link"],
                is_video=media["is_video"]
            )
            for media in request.json["recipe"]["media"]
        ]

        db.session.add_all(new_ingredients)
        db.session.add_all(new_instructions)
        db.session.add_all(new_media)
        db.session.commit()

        return jsonify(recipe={
            "uid": uid,
            "pk": new_recipe.pk,
            "upload_successful": True
        })



def user_can_view_recipe(key):
    """
        Checks to see if a user is allowed to view a recipe with a given key.
    """

    include_private = False
    private_uid = -1
    # if the current user logged in?
    if current_user.is_authenticated:

        include_private = True
        private_uid = current_user.get_id()

    query = Recipe.query.filter(Recipe.pk == key)
    result = query.first()

    # Are we logged in and allowed to view private recipes?
    if include_private:

        return (
            (not result.is_private)
            or (result.is_private and int(private_uid) == int(result.uploaded_by))
        )
    # If we aren't logged in . . .
    else:

        return (
            not result.is_private
        )
