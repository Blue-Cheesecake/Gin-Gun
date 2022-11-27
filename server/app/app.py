from flask import Flask
from flask_restful import Api
from resources.food_list_resource import FoodListResource

app = Flask(__name__)
api = Api(app)

api.add_resource(FoodListResource, '/')

if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=8080)
