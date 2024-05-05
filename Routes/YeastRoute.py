from flask import jsonify, request
from flask_restful import Resource

from DBController.YeastCollectionController import YeastCollection


class YeastRoute(Resource) :
    def __init__(self) :
        self.__yeastCollection = YeastCollection()
    def get(self, id=None) :
        if id is None :
            return self.__yeastCollection.getAllYeasts()
        else :
            return self.__yeastCollection.getYeastById(id)

    def post(self) :
        data= request.get_json()
        try:
            self.__yeastCollection.insertYeast(data)
            return jsonify({"message" :"Yeast added"})
        except Exception as e:
            return jsonify({"message" :str(e)})

    def delete(self, id=None) :
        if id is not None :
            try:
                self.__yeastCollection.deleteYeast(id)
                return jsonify({"message" :"Yeast with id " + id + " deleted"})
            except Exception as e:
                return jsonify({"message" :str(e)})
        else :
            return jsonify({"message" :"Delete Hello, World!"})


    def patch(self, id=None):
        if id is not None:
            data = request.get_json()
            try:
                self.__yeastCollection.updateYeast(id, data)
                return jsonify({"message": "Yeast with id " + id + " updated"})
            except Exception as e:
                return jsonify({"message": str(e)})
        else:
            return jsonify({"message": "No id provided"})