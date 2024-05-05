import uuid
from DBController.MongoDBBaseController import MongoDBBaseController
from Schema.SchemaValidator import SchemaValidator

class YeastCollection(MongoDBBaseController):
    def __init__(self):
        super().__init__("yeast")
        self.schemaValidator=SchemaValidator('Schema/yeast_schema.json')

    def insertYeast(self, data):
        if self.schemaValidator.validateJson(data) :
            return super().insert(data)
        else :
            print("Data is not valid")

    def deleteYeast(self, id):
        return super().delete(id)

    def getAllYeasts(self):
        return super().getAll()

    def getYeastById(self, id):
        return super().getById(id)

    def updateYeast(self, id, data) :
        return super().update(id, data)

