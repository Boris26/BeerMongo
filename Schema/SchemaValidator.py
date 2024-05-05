import json
from jsonschema import validate

class SchemaValidator:

  import json
from jsonschema import validate

class SchemaValidator:
    def __init__(self, schema):
        self.schema = self.load_schema(schema)

    def load_schema(self, schema):
        with open(schema, 'r') as file:
            return json.load(file)

    def validateJson(self, data):
        try:
            validate(instance=data, schema=self.schema)
            return True
        except Exception as e:
            print(e)
            return False