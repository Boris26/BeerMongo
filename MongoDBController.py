import uuid

from pymongo import MongoClient
from Schema import SchemaValidator


class MongoDBController :
    def __init__(self) :
        self.schemaValidator=SchemaValidator.SchemaValidator()
        try :
            self.client=MongoClient('192.168.178.72', 27017)
            self.db=self.client['Beer']
            self.collection=self.db['beer']
        except Exception as e :
            print(e)

    def insert(self, data) :
        if self.schemaValidator.validateJson(data) :
            data['id']=str(uuid.uuid4())
            self.collection.insert_one(data)
        else :
            print("Data is not valid")

    def find(self, query) :
        return self.collection.find(query)

    def update(self, query, data) :
        self.collection.update(query, data)

    def delete(self, id) :
        self.collection.delete_one({'id' : id})

    def getAllRecipes(self) :
        rezepte = list(self.collection.find({}, {'_id' :0}))
        return rezepte

    def getRecipeById(self, id) :
        rezept = self.collection.find_one({'id' :id}, {'_id' :0})
        return rezept

