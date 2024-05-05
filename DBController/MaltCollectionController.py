import uuid
from DBController.MongoDBBaseController import MongoDBBaseController
from Schema.SchemaValidator import SchemaValidator

class MaltCollection(MongoDBBaseController):

    def __init__(self):
        super().__init__("malt")
        self.schemaValidator=SchemaValidator('Schema/malt_schema.json')

    def insertMalt(self, data):
        if self.schemaValidator.validateJson(data):
            return super().insert(data)
        else :
            print("Data is not valid")

    def deleteMalt(self, id):
        return super().delete(id)

    def getAllMalts(self):
        return super().getAll()

    def getMaltById(self, id):
        return super().getById(id)

    def updateMalt(self, id, data) :
        return super().update(id, data)
