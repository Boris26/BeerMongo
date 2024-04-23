from flask import jsonify, request
from flask_restful import Resource
from MongoDBController import MongoDBController

class RecipesRoute(Resource) :
    def get(self, id=None) :
        if id is None :
            return self.__getAllRecipes()
        else :
            return self.__getRecipeById(id)

    def post(self) :
        """Add a new recipe to the database"""
        data=request.get_json()
        try:
            self.__addNewRecipe(data)
            return jsonify({"message" :"Recipe added"})
        except Exception as e:
            return jsonify({"message" :str(e)})

    def delete(self, id=None) :
        """Delete a recipe by id from the database"""
        if id is not None :
            try:
                mongo = MongoDBController()
                mongo.delete(id)
                return jsonify({"message" :"Recipe with id " + id + " deleted"})
            except Exception as e:
                return jsonify({"message" :str(e)})
        else :
            return jsonify({"message" :"Delete Hello, World!"})

    def patch(self) :
        return jsonify({"message" :"Patch Hello, World!"})

    def __getAllRecipes(self):
        """Get all recipes from the database"""
        mongo = MongoDBController()
        return mongo.getAllRecipes()

    def __getRecipeById(self, id):
        """Get a recipe by id from the database"""
        mongo = MongoDBController()
        return mongo.getRecipeById(id)


    def __addNewRecipe(self, data):
        """Add a new recipe to the database"""
        mongo = MongoDBController()
        return mongo.insert(data)
