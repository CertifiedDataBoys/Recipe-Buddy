from flask import Blueprint, jsonify, request
from ...models import db, User, UserProfile


bp = Blueprint("api_v1_users", __name__)


@bp.route("/api/v1.0.0/public/user/get_single_user")
def get_single_user():
    """
        Create a blueprint to get a single user as a JSON file.
        This takes in a user's uid (?uid=<...>) and/or username
        (username=<...>).
    """

    key = request.args.get("uid")
    username = request.args.get("username")


    # error handling --- improve later
    if not key and not username:

        return jsonify(user = [])


    query = db.session.query(User) \
            .join(UserProfile, UserProfile.uid == User.uid)


    if key:

        query = query.filter(User.uid == key)

    if username:

        query = query.filter(User.username == username)

    query = query.with_entities(
        User.uid, User.username, User.verified,
        UserProfile.favorite_recipe, UserProfile.has_profile_photo
    )


    u = query.first()


    # nothing found
    if not u:

        return jsonify(user = [])


    return jsonify(user =
        {
            "uid": u.uid,
            "username": u.username,
            "verified": u.verified,
            "favorite_recipe": u.favorite_recipe,
            "has_profile_photo": u.has_profile_photo
        }
    )
