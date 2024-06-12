from SimplePyLoggerTool import logger, LogLevel
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Routes.RecipesRoute import RecipesRoute
from Routes.MaltRoute import MaltRoute
from Routes.HopsRoute import HopsRoute
from Routes.YeastRoute import YeastRoute
from Routes.BeerTypeRoute import BeerTypeRoute
from Routes.IngredientsRoute import IngredientsRoute

app = Flask(__name__)
CORS(app)
api = Api(app)
logger.log(LogLevel.INFO, "********* Logger initialized *********")
api.add_resource(RecipesRoute, '/recipes', '/recipes/id:<string:id>')
api.add_resource(MaltRoute, '/malt' , '/malt/id:<string:id>')
api.add_resource(HopsRoute, '/hops' , '/hops/id:<string:id>')
api.add_resource(YeastRoute, '/yeast', '/yeast/id:<string:id>')
api.add_resource(BeerTypeRoute, '/beertype', '/beertype/id:<string:id>')
api.add_resource(IngredientsRoute, '/ingredients', '/ingredients/id:<string:id>')

if __name__ == '__main__' :
    app.run(debug=True)
