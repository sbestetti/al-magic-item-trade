from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    SelectField,
    IntegerField
    )
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange


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
            Length(6, 35)
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


class Character_Form(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired("Name required"),
            Length(3, 60)
        ]
    )
    main_class = SelectField(
        "Main class",
        choices=[
            ("Barbarian", "Barbarian"),
            ("Bard", "Bard"),
            ("Cleric", "Cleric"),
            ("Druid", "Druid"),
            ("Fighter", "Fighter"),
            ("Monk", "Monk"),
            ("Paladin", "Paladin"),
            ("Ranger", "Ranger"),
            ("Rogue", "Rogue"),
            ("Sorcerer", "Sorcerer"),
            ("Warlock", "Warlock"),
            ("Wizard", "Wizard")
        ]
    )

    level = IntegerField("Level", validators=[
        NumberRange(1, 20, "Between 1 and 20")
    ])

    race = SelectField(
        "Race",
        choices=[
            ("Dragonborn", "Dragonborn"),
            ("Dwarf", "Dwarf"),
            ("Elf", "Elf"),
            ("Gnome", "Gnome"),
            ("Half-elf", "Half-elf"),
            ("Halfling", "Halfling"),
            ("Hal-orc", "Hal-orc"),
            ("Human", "Human"),
            ("Tiefling", "Tiefling"),
            ("Sorcerer", "Sorcerer"),
            ("Orc of Exandria", "Orc of Exandria")
        ]
    )

    submit = SubmitField("Create")
