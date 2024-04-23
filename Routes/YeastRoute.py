from flask import jsonify
from flask_restful import Resource

class YeastRoute(Resource) :
    def get(self) :
        return jsonify({"message" :"Get Hello, World!"})

    def post(self) :
        return jsonify({"message" :"Post Hello, World!"})

    def put(self) :
        return jsonify({"message" :"Put Hello, World!"})

    def delete(self) :
        return jsonify({"message" :"Delete Hello, World!"})

    def patch(self) :
        return jsonify({"message" :"Patch Hello, World!"})