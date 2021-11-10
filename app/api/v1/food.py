from flask import Blueprint, jsonify, request
from ...models import (
    Ingredient, Kitchenware
)


bp = Blueprint("api_v1_food", __name__)


@bp.route("/api/v1.0.0/public/food/get_ingredient")
def get_ingredient():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = Ingredient.query.filter(Ingredient.pk == key)
    return jsonify(ingredient = query.first())


@bp.route("/api/v1.0.0/public/food/get_kitchenware")
def get_kitchenware():

    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = Kitchenware.query.filter(Kitchenware.pk == key)
    return jsonify(kitchenware = query.first())
