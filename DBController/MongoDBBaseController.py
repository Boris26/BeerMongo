import uuid

from pymongo import MongoClient
from Schema import SchemaValidator


class MongoDBBaseController :
    def __init__(self, collectionName) :
        try :
            self.client=MongoClient('192.168.178.72', 27017)
            self.db=self.client['Beer']
            self.collection=self.collection=self.db[collectionName]
        except Exception as e :
            print(e)

    def insert(self, data) :
        try:
            self.collection.insert_one(data)
            data['id']=str(uuid.uuid4())
            return data
        except Exception as e :
            print(e)
            return False

    def delete(self, id) :
        self.collection.delete_one({'id' :id})

    def getAll(self) :
        return list(self.collection.find({}, {'_id' :0}))

    def getById(self, id) :
        return self.collection.find_one({'id' :id}, {'_id' :0})

    def update(self, id, data) :
        return self.collection.update_one({'id' :id}, {'$set' :data}, upsert = False)



