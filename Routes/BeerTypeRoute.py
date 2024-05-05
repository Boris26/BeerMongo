from flask import jsonify, request
from flask_restful import Resource

from DBController.BeerTypeCollectionController import BeerTypeCollectionController

class BeerTypeRoute(Resource):
    def __init__(self):
        self.beerTypeCollection = BeerTypeCollectionController()
    def get(self):
        return self.beerTypeCollection.getAllBeerTypes()

    def post(self):
        data = request.get_json()
        return self.beerTypeCollection.insertBeerType(data)

