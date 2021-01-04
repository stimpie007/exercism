class Allergies:
    """
    Contains a score and allergies

    :param:
    score: int
    allergies: dict
    """
    def __init__(self, score: int):
        self.score = score
        self.allergies = {"eggs": 1,
                          "peanuts": 2,
                          "shellfish": 4,
                          "strawberries": 8,
                          "tomatoes": 16,
                          "chocolate": 32,
                          "pollen": 64,
                          "cats": 128}

    def allergic_to(self, item):
        """
        Check if you are allergic to item

        :param
        item: str

        :return:
        bool
        """
        return bool(self.score & self.allergies.get(item, 0))

    @property
    def lst(self):
        """
        List of items you are allergic to

        :return:
        list
        """
        return [key for key in self.allergies if self.allergic_to(key)]
