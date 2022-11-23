from .food_model import FoodModel


class FoodListModel:

  foodList: list[FoodModel]

  def __init__(self, foodList: list[FoodModel] = [], *args) -> None:
    if len(foodList) == 0 and len(args) == 0:
      raise Exception("No Data provided in List")
    if len(foodList) != 0 and len(args) != 0:
      raise Exception("Select only one way to insert data")
    if len(foodList) == 0:
      self.foodList = [each for each in args]
    if len(args) == 0:
      self.foodList = foodList

  def json(self) -> dict[str: str]:
    return {
        'foodList': [food.json() for food in self.foodList]
    }
