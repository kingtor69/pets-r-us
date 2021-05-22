from app import app
from models import db, Pet


db.drop_all()
db.create_all()

Pet.query.delete()

seed_pets = [
    Pet(name="Scaredy Cat", species="cat", photo_url = "https://images.unsplash.com/photo-1548247416-ec66f4900b2e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=663&q=80", age="10", notes="This sweet little thing is afraid of her own shadow."),
    Pet(name="Stretch Armstrong", species="cat", photo_url = "https://images.unsplash.com/photo-1571566882372-1598d88abd90?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2134&q=80", age="2"),
    Pet(name="Butthead", species="dog", notes="gets along very well with his kittie friend Beavis, recommend they are adopted together"),
    Pet(name="Beavis", species="cat", notes="loves his doggie friend Butthead, reommend they are adopted together"),
    Pet(name="Cutie Pie", species="cat", photo_url = "https://images.unsplash.com/photo-1533743983669-94fa5c4338ec?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=983&q=80", age="3", is_years=False, notes="How can you say no to that face‽"),
    Pet(name="Bowie", species="Collie dog", photo_url = "https://lh3.googleusercontent.com/o1lVJfNBakL0NqgrjAhxN_tiIbFEI6mCoHPNg-Sbgx9GdqnY-4UDDKZ6EODM7fpb7sZ9i9J0lSA-w3IUUjFj9ML7RPe0ihcHdRVzH5kcsceSDu43B_OapJKziUyO1P5Lz3cxSZFBkNwVr_uZe-hSaZeaRYJBdnl94i--S5p5_c1nWt4OZmQQ0fwmj-kWvFVmW__3K11PmoD6fNB65qGAMsHUxjCqJmlcqQQziF7qFWXio0MbW3w4PcD-m7a5lk602l0UnilHptfoWC0Za6nBVTS6-4Ib2Zcx7KoihGA3P5gy5TUZRKEqnsm1gjWiBkcyaE0toeKVdMdfratzujFKHPNuTXrOy2zTI67v4JdFNnLbwTo4Aq_9KFSqtDTJnqrkSxoKtgUnZKSN6bGFfMB4TGGQ0ln4SEAwyW4E8YjGMuPyVLmHbWItyYPYQqKnfeffnNU8rFYj71PtPi3pL5XeHZu5yAr604cFaJ9KryKOVUGYzZ7iFkXTE2kWRIeRODi5-j5Fa1dfi1R-ocSNsEpkKjxva63EzmhnnxVQTJBeUER7_Mvg4QOgrWvr-L17oxlI8D5T5qplgpnc1QMUNOOKYZQ-_59TkXVJU9TayQS1Af8pubU8eb7jgmnZZRY3LIckkyqYa5PFdwsYarX6FXdvv7_Mxx4EE1uswcNLdNXCXvFrwM9QaYrCbAd_dcDFa7ln4wFzDtHd45ViKgV1KdfSiKmF1A=w683-h888-no?authuser=0", age="9", notes="Best Dog Ever", is_available=False)
]

db.session.add_all(seed_pets)
db.session.commit()