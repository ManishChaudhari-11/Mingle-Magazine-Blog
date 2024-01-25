from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    ValidationError,
)
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    category = SelectField(
        choices=(
            ("Select Category", "Select Category"),
            ("Food", "Food"),
            ("Travel", "Travel"),
            ("Lifestyle", "Lifestyle"),
            ("Fashion", "Fashion"),
            ("Fitness", "Fitness"),
            ("Music", "Music"),
            ("Sports", "Sports"),
            ("Technology", "Technology"),
            ("Politics", "Politics"),
            ("Business", "Business"),
            ("Education", "Education"),
            ("Health", "Health"),
            ("Science", "Science"),
            ("Entertainment", "Entertainment"),
            ("Art", "Art"),
            ("Culture", "Culture"),
            ("Religion", "Religion"),
            ("History", "History"),
            ("Nature", "Nature"),
            ("Personal Finance", "Personal Finance"),
        ),
        validators=[DataRequired()],
        default="Select Category",
    )
    tagline = StringField("Tagline", validators=[DataRequired()])
    content = CKEditorField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")

    def validate_category(self, category):
        if category.data == "Select Category":
            raise ValidationError("Please select a category.")
