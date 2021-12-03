from flask import Blueprint, jsonify, request
from flask_login import current_user
from ...models import db, User, UserProfile
from werkzeug.utils import secure_filename
import os
import base64

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

        return jsonify(user=[])

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

        return jsonify(user=[])

    return jsonify(user={
            "uid": u.uid,
            "username": u.username,
            "verified": u.verified,
            "favorite_recipe": u.favorite_recipe,
            "has_profile_photo": u.has_profile_photo
        }
    )


@bp.route("/api/v1.0.0/public/user/get_user_profile_photo")
def get_user_profile_photo():
    """
        Return the URL to a user's profile photo.
        If the user does not have a profile photo, return the URL
        or the default profile photo.
        This takes in a user's uid (?uid=<...>) and/or username
        (username=<...>).
    """

    key = request.args.get("uid")
    username = request.args.get("username")

    # error handling --- improve later
    if not key and not username:

        return jsonify(user=[])

    query = db.session.query(User) \
            .join(UserProfile, UserProfile.uid == User.uid)

    if key:

        query = query.filter(User.uid == key)

    if username:

        query = query.filter(User.username == username)

    query = query.with_entities(
        User.uid,
        UserProfile.has_profile_photo
    )

    u = query.first()

    # nothing found
    if not u:

        return jsonify(user=[])

    profile_photo_url = ""

    # something found
    if u.has_profile_photo:

        profile_photo_url = "/res/profile_photos/{0}.png".format(u.uid)

    else:

        profile_photo_url = "/res/profile_photos/default.png"

    return jsonify(user={
        "uid": u.uid,
        "has_profile_photo": u.has_profile_photo,
        "profile_photo_url": profile_photo_url
    })


@bp.route("/api/v1.0.0/public/user/upload_user_profile_photo", methods=['GET', 'POST'])
def upload_user_profile_photo():
    # Is this user not logged in?
    if not current_user.is_authenticated:
        return jsonify(user=[])

    if request.method == "POST":

        uid = current_user.get_id()

        query = db.session.query(User) \
                .join(UserProfile, UserProfile.uid == User.uid) \
                .filter(User.uid == uid) \
                .with_entities(
                    User.uid, User.username,
                    UserProfile.has_profile_photo
                )
        u = query.first()

        # No file uploaded
        if "profile_image" not in request.json:

            return jsonify(user={
                "uid": u.uid,
                "username": u.username,
                "has_profile_photo": u.has_profile_photo,
                "upload_successful": False
            })

        # Check whether the specified path exists or not
        if not os.path.exists("/data/profile_photos/"):
            # Create a new directory because it does not exist
            os.makedirs("/data/profile_photos/")

        if request.json["profile_image"].startswith("data:image/png;base64,"):
            request.json["profile_image"] = request.json["profile_image"][22:]
        imgdata = base64.b64decode(request.json["profile_image"])
        with open("/data/profile_photos/" + uid + ".png", 'wb') as f:
            f.write(imgdata)

        user = User.query.filter(User.uid == uid).first()

        user_profile = UserProfile.query.filter(
            UserProfile.uid == uid).first()
        user_profile.has_profile_photo = True

        db.session.commit()

        return jsonify(user={
            "uid": user.uid,
            "username": user.username,
            "has_profile_photo": user_profile.has_profile_photo,
            "upload_successful": True
        })

