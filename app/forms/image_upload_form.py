from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class ImageUploadForm(FlaskForm):
    """
        This Form handles user comments on recipe pages

        Attributes:
            image_field (FileField):
                        Input for an image file
            submit (SubmitField):
                        Button to submit the image to RecipeBuddy
    """

    image_field = FileField(validators=[FileRequired()])
    submit = SubmitField("Upload image")
