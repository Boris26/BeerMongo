from flask import jsonify, request
from flask_restful import Resource

from DBController.HopsCollectionController import HopsCollection


class HopsRoute(Resource) :
    def __init__(self) :
        self.__hopsCollection = HopsCollection()
    def get(self, id=None) :
        if id is None :
            return jsonify(self.__hopsCollection.getAllHops())
        else :
            return self.__hopsCollection.getHopById(id)


    def post(self) :
        data = request.get_json()
        return self.__hopsCollection.insertHop(data)

    def delete(self, id=None) :
        """Delete a recipe by id from the database"""
        if id is not None :
            try :
                self.__hopsCollection.deleteHop(id)
                return jsonify({"message" :"Recipe with id " + id + " deleted"})
            except Exception as e :
                return jsonify({"message" :str(e)})
        else :
            return jsonify({"message" :"Delete Hello, World!"})

    def patch(self, id=None) :
        if id is not None :
            data = request.get_json()
            try :
                self.__hopsCollection.updateHop(id, data)
                return jsonify({"message" :"Hop with id " + id + " updated"})
            except Exception as e :
                return jsonify({"message" :str(e)})
        else :
            return jsonify({"message" :"No id provided"})
