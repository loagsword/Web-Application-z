import json

from flask import request

from . import create_app
from .models import request


app = create_app()


@app.route('/', methods=['GET'])
def fetch():
    cats - Cats.query.all()
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed,
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200

@app.route('/', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    cat = Cats(name=name, price-price, breed=breed)
    db.session.add(cat)
    db.session.commit()
    return json.dumps("Added"), 200

@app.route('/remove/<cat_id', methods=['DELETE'])
def remove(cat_id):
    Cats.query.filter_by(id=cat_id).delete()
    db.session.commit()
    return json.dumps("Deleted"), 200

