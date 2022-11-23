from models.food_list_model import FoodListModel
from models.food_model import FoodModel


def getFoodListData() -> FoodListModel:

  li = [
      FoodModel("Curry", "main"),
      FoodModel("Sashimi Salmon", "appertizer"),
      FoodModel("Angus Steak", "meat"),
      FoodModel("Cheese Ice-scream", "dessert")
  ]

  return FoodListModel(foodList=li)
