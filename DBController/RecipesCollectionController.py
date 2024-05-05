import uuid

from DBController.MongoDBBaseController import MongoDBBaseController
from Schema.SchemaValidator import SchemaValidator


class RecipesCollection(MongoDBBaseController):
    def __init__(self):
        super().__init__("recipes")
        self.schemaValidator=SchemaValidator('Schema/recipes_schema.json')

    def insertRecipe(self, data):
        if self.schemaValidator.validateJson(data) :
            try:
                data['id'] = str(uuid.uuid4())
                super().insert(data)
                return str(data)
            except Exception as e:
                return str(e)
        else :
            return "Data is not valid"

    def deleteRecipe(self, id) :
        return super().delete(id)

    def getAllRecipes(self) :
        return super().getAll()

    def getRecipeById(self, id) :
         return super().getById(id)

    def updateRecipe(self, id, data) :
        return super().update(id, data)
