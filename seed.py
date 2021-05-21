from app import app
from models import db, Pet


db.drop_all()
db.create_all()

Pet.query.delete()

seed_pets = [
    Pet(name="Scaredy Cat", species="cat", photo_url = "https://images.unsplash.com/photo-1548247416-ec66f4900b2e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=663&q=80", age="10", notes="This sweet little thing is afraid of her own shadow.", available=True),
    Pet(name="Stretch Armstrong", species="cat", photo_url = "https://images.unsplash.com/photo-1571566882372-1598d88abd90?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2134&q=80", age="2", available=True),
    Pet(name="Butthead", species="dog", notes="gets along very well with his kittie friend Beavis, recommend they are adopted together"),
    Pet(name="Beavis", species="cat", notes="loves his doggie friend Butthead, reommend they are adopted together"),
    Pet(name="", species="cat", photo_url = "https://images.unsplash.com/photo-1533743983669-94fa5c4338ec?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=983&q=80", age=".3", notes="How can you say no to that face‽", available=True),
    Pet(name="Bowie", species="Collie dog", photo_url = "https://photos.app.goo.gl/GarFwioQTPVZSJdaA", age="9", notes="Best Dog Ever", available=False)
]

db.session.add_all(seed_pets)
db.session.commit()