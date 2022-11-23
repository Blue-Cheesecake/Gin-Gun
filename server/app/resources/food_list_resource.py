from flask_restful import Resource
from typing import Dict
from data.fake_food_list_data import getFoodListData


class FoodListResource(Resource):

  def get(self) -> Dict:
    """Get list of foods

    Returns:
        Dict: Json Format
    """
    return getFoodListData().json()
