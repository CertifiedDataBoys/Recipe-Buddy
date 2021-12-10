from flask import Blueprint, jsonify, request
from ...models import (
    db, Ingredient, Kitchenware
)


bp = Blueprint("api_v1_food", __name__)

@bp.route("/api/v1.0.0/public/food/create_ingredient", methods=["POST"])
def create_ingredient():
    """
        Create a blueprint to create a single recipe
    """
    data = request.get_json()

    if not data or not data.get("name") or not data.get("unit_of_measure") or not data.get("units_plural"):
        return jsonify({"success": False, "error": "Missing data"})

    ingredient = Ingredient(
        name=data["name"],
        unit_of_measure=data["unit_of_measure"],
        units_plural=data["units_plural"]
    )
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({"success": True})

@bp.route("/api/v1.0.0/public/food/update_ingredient", methods=["POST"])
def update_ingredient():
    """
        Create a blueprint to update a single recipe
    """

    data = request.get_json()
    key = request.args.get("pk")

    if not data or not data.get("name") or not data.get("unit_of_measure") or not data.get("units_plural"):
        return jsonify({"success": False, "error": "Missing data"})

    if not key:
        return jsonify({"success": False, "error": "Missing key"})
    
    Ingredient.query.\
        filter(Ingredient.pk == key).\
        update({Ingredient.name: data["name"], Ingredient.unit_of_measure: data["unit_of_measure"], Ingredient.units_plural: data["units_plural"]})
    db.session.commit()
    return jsonify({"success": True})

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

@bp.route("/api/v1.0.0/public/food/create_kitchenware", methods=["POST"])
def create_kitchenware():
    """
        Create a blueprint to create a single recipe
    """
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"success": False, "error": "Missing data"})

    kitchenware = Kitchenware(
        name=data["name"]
    )
    db.session.add(kitchenware)
    db.session.commit()
    return jsonify({"success": True})

@bp.route("/api/v1.0.0/public/food/update_kitchenware", methods=["POST"])
def update_kitchenware():
    """
        Create a blueprint to update a single recipe
    """

    data = request.get_json()
    key = request.args.get("pk")

    if not data or not data.get("name"):
        return jsonify({"success": False, "error": "Missing data"})

    if not key:
        return jsonify({"success": False, "error": "Missing key"})
    
    Kitchenware.query.\
        filter(Kitchenware.pk == key).\
        update({Kitchenware.name: data["name"]})
    db.session.commit()
    return jsonify({"success": True})

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
