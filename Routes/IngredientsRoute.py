from flask import jsonify, request
from flask_restful import Resource

from DBController.IngredientsCollectionController import IngredientsCollection


class IngredientsRoute(Resource) :

    def __init__(self) :
        self.IngrediensCollection=IngredientsCollection()

    def get(self, id=None) :
        if id is None :
            return jsonify(self.IngrediensCollection.getAllIngredients())
        else :
            return self.IngrediensCollection.getIngredientById(id)

    def post(self) :
        data=request.get_json()
        return self.IngrediensCollection.insertIngredient(data)
