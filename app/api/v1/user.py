from flask import Blueprint, jsonify, request
from flask_login import current_user
from ...models import db, User, UserProfile
from werkzeug.utils import secure_filename


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

        return jsonify(user = [])


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

        return jsonify(user = [])


    profile_photo_url = ""

    # something found
    if u.has_profile_photo:

        profile_photo_url = "/res/profile_photos/{0}.png".format(u.uid)

    else:

        profile_photo_url = "/res/profile_photos/default.png"

    return jsonify(user = {
        "uid": u.uid,
        "has_profile_photo": u.has_profile_photo,
        "profile_photo_url": profile_photo_url
    })


@bp.route("/api/v1.0.0/public/user/upload_user_profile_photo", methods=['GET', 'POST'])
def upload_user_profile_photo():

    # Is this user not logged in?
    if not current_user.is_authenticated:
        return jsonify(user = [])

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
        import sys
        print(request.files, file=sys.stderr)
        if "image_field" not in request.files:

            return jsonify(user = {
                "uid": u.uid,
                "username": u.username,
                "has_profile_photo": u.has_profile_photo,
                "upload_successful": False
            })

        file = request.files["image_field"]

        # No filename
        if file.filename == "":

            return jsonify(user = {
                "uid": u.uid,
                "username": u.username,
                "has_profile_photo": u.has_profile_photo,
                "upload_successful": False
            })

        # File given, filename is good
        if file and "." in file.filename \
                and file.filename.rsplit('.', 1)[1].lower() == "png":

            final_filename = uid + ".png"
            file.save("./public/res/profile_photos/" + final_filename)

            user = User.query.filter(User.uid == uid).first()

            user_profile = UserProfile.query.filter(UserProfile.uid == uid).first()
            user_profile.has_profile_photo = True

            db.session.commit()

            return jsonify(user = {
                "uid": user.uid,
                "username": user.username,
                "has_profile_photo": user_profile.has_profile_photo,
                "upload_successful": True
            })

        # Something wen wrong
        else:

            return jsonify(user = {
                "uid": u.uid,
                "username": u.username,
                "has_profile_photo": u.has_profile_photo,
                "upload_successful": False
            })
