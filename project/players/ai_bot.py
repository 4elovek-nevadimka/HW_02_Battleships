from project.logic.desk import Desk
from project.players.player import Player


class AiBot(Player):

    def __init__(self, name):
        super().__init__(name)
        self._enemy_desk = Desk("Моё игровое поле")

    def get_point(self):
        return self.enemy_desk.get_random_coordinates()
