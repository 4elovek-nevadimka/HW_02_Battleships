from project.logic.desk import Desk
from project.players.player import Player


class User(Player):

    def __init__(self, name):
        super().__init__(name)
        self._enemy_desk = Desk("Поле противника")

    def get_point(self):
        row = self.input_data(f"Игрок {self.name}, сделайте ход. Укажите строку: ")
        col = self.input_data(f"Теперь укажите столбец: ")
        return row, col

    def input_data(self, message):
        while True:
            try:
                input_value = int(input(message))
                if input_value > self.enemy_desk.FIELD_SIZE or input_value < 1:
                    print(f"Укажите число от 1 до {self.enemy_desk.FIELD_SIZE}.")
                else:
                    return input_value
            except ValueError:
                print(f"Ошибка! Укажите число от 1 до {self.enemy_desk.FIELD_SIZE}.")
