from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea


class CommentForm(FlaskForm):
    """
        This Form handles user comments on recipe pages

        Attributes:
            contents (StringField):
                        Input for a comment's contents
            submit (SubmitField):
                        Button to submit the comment to RecipeBuddy
    """

    contents = StringField("Comment",
                           validators=[
                               DataRequired(),
                               Length(max=1024,
                                      message="Comments can be no more than 1024 characters long!"
                                      )
                           ],
                           widget=TextArea())
    submit = SubmitField("Post comment")
