import json

from flask import jsonify, request, Response
from flask_restful import Resource

from DBController.RecipesCollectionController import RecipesCollection


class RecipesRoute(Resource) :

    def __init__(self) :
        self.__recipes = RecipesCollection()
    def get(self, id=None) :
        if id is None :
            return jsonify(self.__recipes.getAllRecipes())
        else :
            return self.__recipes.getRecipeById(id)

    def post(self) :
        """Add a new recipe to the database"""
        data=request.get_json()
        try:
            result = self.__recipes.insertRecipe(data)
            if result:
                return Response(status=201, mimetype='application/json')
            else:
                return Response(json.dumps({"message" :result}), status=400, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({"message" : e}), status=400, mimetype='application/json')


    def delete(self, id=None) :
        """Delete a recipe by id from the database"""
        if id is not None :
            try:
                self.__recipes.deleteRecipe(id)
                return jsonify({"message" :"Recipe with id " + id + " deleted"})
            except Exception as e:
                return jsonify({"message" :str(e)})
        else :
            return jsonify({"message" :"Delete Hello, World!"})

    def patch(self, id=None) :
        if id is not None :
            data = request.get_json()
            try :
                self.__recipes.updateRecipe(id, data)
                return jsonify({"message" :"Recipe with id " + id + " updated"})
            except Exception as e :
                return jsonify({"message" :str(e)})
        else :
            return jsonify({"message" :"No id provided"})



