from flask_wtf import Form

from wtforms import StringField, PasswordField, validators


class Registration_Form(Form):
    name = StringField(
        "Name",
        [validators.Length(4, 100, "Has to be between 4 and 100 characters")]
        )
    email = StringField("Email", [validators.Length(min=6, max=35)])
    dci = StringField("DCI", [validators.Length(min=6, max=35)])
    password = PasswordField(
        "Password",
        [validators.equal_to("confirm_password", "Passwords don't match")]
        )
    confirm_password = PasswordField("Re-type password")
