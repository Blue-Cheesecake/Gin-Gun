from flask import Flask, render_template
from flask_restful import Api
from data.fake_food_list_data import getFoodListData


app = Flask(__name__)
api = Api(app)


@app.route("/")
def homepage():
  return render_template("index.html", foodlist=getFoodListData().json()['foodList'])


if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=8080)
