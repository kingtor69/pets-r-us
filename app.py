from flask import Flask,request,redirect,render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
# from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_r_us_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "bigbadsecretf0nziemuthafukka!"

connect_db(app)

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def show_home_page():
    pets = Pet.query.all()
    any_pets_avail = False
    for pet in pets:
        if pet.is_available:
            any_pets_avail = True
    return render_template('home.html', pets=pets, any_pets_avail=any_pets_avail)

@app.route('/pets/new', methods = ["GET", "POST"])
def add_new_pet():
    form = AddPetForm(is_years=True, is_available=True)
    if form.validate_on_submit():
        # do some fucking thing
        return redirect('/')
    else:
        return render_template('new-pet-form.html')

