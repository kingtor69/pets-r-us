from flask import Flask,request,redirect,render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_r_us_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "bigbadsecretf0nziemuthafukka!"

connect_db(app)

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
# def show_home_page():
#     """show all pets' pictures, names and adoption status"""
#     pets = Pet.query.all()
#     any_pets_avail = False
#     for pet in pets:
#         if pet.is_available:
#             any_pets_avail = True
#     return render_template('home.html', pets=pets, any_pets_avail=any_pets_avail)
def show_sorted_home_page():
    """sort pets in to adoptable (first) and unadoptable (second), then display pictures and names along with that adoption status"""
    avail_pets = Pet.query.filter_by(is_available=True)
    any_pets_avail = False
    for pet in avail_pets:
        any_pets_avail=True
    unavail_pets = Pet.query.filter_by(is_available=False)
    return render_template('sorted-pets.html', pets=[avail_pets, unavail_pets], any_pets_avail=any_pets_avail)

@app.route('/add', methods = ["GET", "POST"])
def add_new_pet():
    """Displays a new pet form and then adds the returned data, if authenticated, to the database. Reloads form if data is not valid."""
    form = PetForm(is_years=True, is_available=True)
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        is_years = form.is_years.data
        notes = form.notes.data
        is_available = form.is_available.data
        # there's gotta be an easier way to do this, right?
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, is_years=is_years, notes=notes, is_available=is_available)
        db.session.add(pet)
        db.session.commit()
        flash(f'Successfully added {pet.name}', 'success')
        return redirect('/')
    else:
        return render_template('new-pet-form.html', form=form)

@app.route("/<int:id>", methods=['GET', 'POST'])
def display_pet_info(id):
    """displays a card of pet information and an edit button to change that information"""
    pet = Pet.query.get(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.is_years = form.is_years.data
        pet.notes = form.notes.data
        pet.is_available = form.is_available.data
        db.session.add(pet)
        db.session.commit()
        flash(f"Successfully edited {pet.name}'s info", 'success')
        return redirect(f'/{pet.id}')
    else: 
        return render_template('pet-info.html', form=form, pet=pet)

@app.route("/<int:id>/edit")
def load_edit_form(id):
    """load the PetForm pre-populated to edit info"""
    pet = Pet.query.get(id)
    form = PetForm(obj=pet)
    return render_template('edit-pet-form.html', form=form, pet=pet)