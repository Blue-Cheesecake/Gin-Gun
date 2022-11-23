class FoodModel:

  def __init__(self, name: str, category: str) -> None:
    self.name: str = name
    self.category: str = category

  def json(self) -> dict[str: str]:
    return {
        'name': self.name,
        'category': self.category
    }
