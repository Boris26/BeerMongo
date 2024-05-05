import uuid

from DBController.MongoDBBaseController import MongoDBBaseController
from Schema.SchemaValidator import SchemaValidator


class BeerTypeCollectionController(MongoDBBaseController):
    def __init__(self) :
        super().__init__("beertypes")
        self.schemaValidator=SchemaValidator('Schema/beertype_schema.json')

    def insertBeerType(self, beerType):
        if self.schemaValidator.validateJson(beerType):
            try :
                beerType['id'] = str(uuid.uuid4())
                super().insert(beerType)
                return str(beerType)
            except Exception as e:
                return str(e)
        else :
            return "Data is not valid"

    def getAllBeerTypes(self):
        return super().getAll()
