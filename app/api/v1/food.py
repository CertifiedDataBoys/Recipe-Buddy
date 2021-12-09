from flask import Blueprint, jsonify, request
from ...models import (
    Ingredient, Kitchenware
)


bp = Blueprint("api_v1_food", __name__)


@bp.route("/api/v1.0.0/public/food/get_ingredient")
def get_ingredient():
    """
        Create a blueprint to get a single ingredient as a JSON file.
        This takes in an ingredient's primary key (?pk=<...>).
    """

    key = request.args.get("pk")

    # error handling --- improve later
    if not key:

        return jsonify([])

    query = Ingredient.query.filter(Ingredient.pk == key)
    return jsonify(ingredient=query.first())

@bp.route("/api/v1.0.0/public/food/get_all_ingredients")
def get_all_ingredients():
    """
        Create a blueprint to get all ingredients as a JSON file.
    """

    query = Ingredient.query.all()
    return jsonify(ingredients=query)

@bp.route("/api/v1.0.0/public/food/get_kitchenware")
def get_kitchenware():
    """
        Create a blueprint to get a single kitchenware item as a JSON file.
        This takes in a kitchenware item's primary key (?pk=<...>).
    """

    key = request.args.get("pk")

    # error handling --- improve later
    if not key:

        return jsonify([])

    query = Kitchenware.query.filter(Kitchenware.pk == key)
    return jsonify(kitchenware=query.first())

@bp.route("/api/v1.0.0/public/food/get_all_kitchenware")
def get_all_kitchenware():
    """
        Create a blueprint to get all kitchenware items as a JSON file.
    """

    query = Kitchenware.query.all()
    return jsonify(kitchenware=query)
