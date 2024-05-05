import uuid

from DBController.MongoDBBaseController import MongoDBBaseController
from Schema.SchemaValidator import SchemaValidator


class HopsCollection(MongoDBBaseController):
    def __init__(self):
        super().__init__("hops")
        self.schemaValidator=SchemaValidator('Schema/hops_schema.json')

    def insertHop(self, data):
        if self.schemaValidator.validateJson(data) :
            try :
                data['id']=str(uuid.uuid4())
                super().insert(data)
                return str(data)
            except Exception as e :
                return str(e)
        else :
            return "Data is not valid"
    def deleteHop(self, id):
        return super().delete(id)

    def getAllHops(self):
        return super().getAll()

    def getHopById(self, id):
        return super().getById(id)

    def updateHop(self, id, data) :
        return super().update(id, data)
