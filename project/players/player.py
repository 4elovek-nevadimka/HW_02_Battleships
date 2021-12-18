from project.custom_exceptions.duplication_exception import DuplicationError
from project.game_log import GameLogger
from project.intro import Intro


class Player:

    def __init__(self, name):
        self._name = name
        self._enemy_desk = None

    def get_point(self):
        raise NotImplementedError()

    def make_a_move(self, other_desk):
        while True:
            coordinates = self.get_point()
            try:
                shoot_result = self._enemy_desk.shoot(coordinates)
            except DuplicationError as ex:
                print(ex)
            else:
                GameLogger.add_move_message(
                    f"игрок {self.name} походил {coordinates[0]} : {coordinates[1]} -->")
                Intro.clear_screen()
                self._enemy_desk.show(other_desk)
                GameLogger.print_log()
                if shoot_result[1]:
                    break
                if shoot_result[0]:
                    print(f"\nИгра окончена. Победил игрок '{self.name}'")
                    break
        return shoot_result[0]

    def __eq__(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self._name

    @property
    def enemy_desk(self):
        return self._enemy_desk
