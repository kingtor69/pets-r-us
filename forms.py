from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, URL, Optional, NumberRange 

class PetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired(message="What kind of animal person are you‽ Pets must have names.")])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("giraffe", "Giraffe")])
    photo_url = StringField("photo_url", validators=[Optional(), URL(message="please enter a valid URL")])
    age = IntegerField("Age", validators=(Optional(), NumberRange(min=0, max=30, message="I do not believe your pet is that age. Please enter a number between 0 and 30")))
    is_years = BooleanField("Age in Years? (Months if unchecked)")
    notes = StringField("notes")
    is_available = BooleanField("Available for Adoption?")
