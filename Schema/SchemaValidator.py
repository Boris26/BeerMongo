import json
from jsonschema import validate

class SchemaValidator:

    def __init__(self):
        with open('/home/boris/Entwicklung/BeerMongo/Schema/recipes_schema.json', 'r') as file:
            self.schema = json.load(file)

    def validateJson(self, data):
        with open('/home/boris/Entwicklung/BeerMongo/Schema/recipes_schema.json', 'r') as file:
            self.schema = json.load(file)
        try:
            validate(instance=data, schema=self.schema)
            return True
        except Exception as e:
            print(e)
            return False