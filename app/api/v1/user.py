from flask import Blueprint, jsonify, request
from ...models import db, User, UserProfile


bp = Blueprint("api_v1_users", __name__)


@bp.route("/api/v1.0.0/public/user/get_single_user")
def get_single_user():
    """
        Create a blueprint to get a single user as a JSON file.
        This takes in a user's uid (?uid=<...>) and/or username (username=<...>).
    """

    key = request.args.get("uid")
    username = request.args.get("username")


    # error handling --- improve later
    if not key and not username:

        return jsonify([])


    query = User.query \
        .with_entities(User.uid, User.username)


    if key:

        query = query.filter(User.uid == key)

    if username:

        query = query.filter(User.username == username)


    u = query.first()


    # nothing found
    if not u:

        return jsonify(user = [])


    return jsonify(user = {"uid": u.uid, "username": u.username})
