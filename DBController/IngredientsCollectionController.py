import uuid

from DBController.MongoDBBaseController import MongoDBBaseController
from Schema.SchemaValidator import SchemaValidator


class IngredientsCollection(MongoDBBaseController):
    def __init__(self) :
        super().__init__("Ingredients")
        self.schemaValidator=SchemaValidator('Schema/ingredients_schema.json')

    def insertIngredient(self, data) :
        if self.schemaValidator.validateJson(data):
            try :
                data['id']=str(uuid.uuid4())
                super().insert(data)
                return str(data)
            except Exception as e:
                return str(e)
        else :
            return "Data is not valid"

    def deleteIngredient(self, id):
        return super().delete(id)

    def getAllIngredients(self):
        return super().getAll()

    def getIngredientById(self, id):
        return super().getById(id)

    def updateIngredient(self, id, data):
        return super().update(id, data)
