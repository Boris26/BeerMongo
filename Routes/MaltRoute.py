from flask import jsonify, request
from flask_restful import Resource

from DBController.MaltCollectionController import MaltCollection


class MaltRoute(Resource) :
    def __init__(self) :
        self.__maltCollection = MaltCollection()
    def get(self, id=None) :
        if id is None :
            return self.__maltCollection.getAllMalts()
        else :
            return self.__maltCollection.getMaltById(id)

    def post(self) :
        data = request.get_json()
        return self.__maltCollection.insertMalt(data)

    def delete(self, id=None) :
        """Delete a malt by id from the database"""
        if id is not None :
            try :
                self.__maltCollection.deleteMalt(id)
                return jsonify({"message" :"Recipe with id " + id + " deleted"})
            except Exception as e :
                return jsonify({"message" :str(e)})
        else :
            return jsonify({"message" :"Delete Hello, World!"})

    def patch(self, id=None) :
        if id is not None :
            data = request.get_json()
            try :
                self.__maltCollection.updateMalt(id, data)
                return jsonify({"message" :"Malt with id " + id + " updated"})
            except Exception as e :
                return jsonify({"message" :str(e)})
        else :
            return jsonify({"message" :"No id provided"})


