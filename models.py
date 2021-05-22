from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect the database to our Flask app."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """sets up Model for pets table, showing details of pets available for adoption"""
    __tablename__ = "pets"

    def __repr__(self):
        """display Pet-modelled object"""
        return f"<id={self.id} name={self.name} species = {self.species} age={self.age} is_available={self.is_available} notes={self.notes} photo_url={self.photo_url}"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer)
    is_years = db.Column(db.Boolean, default=True)
    notes = db.Column(db.String)
    is_available = db.Column(db.Boolean, nullable=False, default=True)