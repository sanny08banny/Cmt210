# app/forms.py
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, FloatField, SubmitField

class AddMenuItemForm(FlaskForm):
    name = StringField('Name')
    description = TextAreaField('Description')
    price = FloatField('Price')
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Add Item')


