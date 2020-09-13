from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    SelectField,
    SubmitField,
    )
from wtforms.validators import DataRequired, Length, EqualTo


class Registration_Form(FlaskForm):
    """ Form class for registering new users """
    name = StringField(
        "Name",
        validators=[
            DataRequired("Name required"),
            Length(4, 100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired("Email required"),
            Length(6, 35)
        ]
    )

    dci = StringField(
        "DCI",
        validators=[
            DataRequired("Email required"),
            Length(6, 35)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired("Password required"),
            Length(4, 16),
            EqualTo("confirm_password", "Passwords don't match")
        ]
    )

    confirm_password = PasswordField("Re-type password")

    submit = SubmitField("Submit")


class Login_Form(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired("Email required"),
            Length(6, 100)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired("Password required"),
            Length(4, 16),
        ]
    )

    submit = SubmitField("Submit")


class New_Item_Form(FlaskForm):
    character = StringField("Character")
    item = SelectField("Item", validators=[DataRequired()])
    submit = SubmitField("Submit")
