from flask import Flask
from flask_restful import Api
from Routes.RecipesRoute import RecipesRoute
from Routes.MaltRoute import MaltRoute
from Routes.HopsRoute import HopsRoute
from Routes.YeastRoute import YeastRoute

app = Flask(__name__)
api = Api(app)

api.add_resource(RecipesRoute, '/recipes', '/recipes/id/<string:id>')
api.add_resource(MaltRoute, '/malt')
api.add_resource(HopsRoute, '/hops')
api.add_resource(YeastRoute, '/yeast')

if __name__ == '__main__' :
    app.run(debug=True)
