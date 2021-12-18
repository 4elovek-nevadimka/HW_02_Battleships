from random import randint

from project.custom_exceptions.duplication_exception import DuplicationError
from project.game_log import GameLogger
from project.logic.point import Point
from project.logic.point_type import PointType
from project.logic.ships import Ships


class Desk:
    FIELD_SIZE = 6

    def __init__(self, name):
        self.points = []
        for i in range(self.FIELD_SIZE):
            for j in range(self.FIELD_SIZE):
                self.points.append(Point(i + 1, j + 1, self))
        self.name = name
        self.ships = Ships(self)

    @property
    def indent(self):
        return 3 + Desk.FIELD_SIZE * 4 - len(self.name)

    @property
    def caption(self):
        return f"  {' ' * (self.indent // 2)} {self.name} {' ' * (self.indent // 2)}"

    def reset_points(self):
        for p in self.points:
            p.reset()

    def is_all_ships_destroyed(self):
        return self.ships.is_all_ships_destroyed()

    def get_random_point(self):
        return self.get_point(self.get_random_coordinates())

    def get_random_coordinates(self):
        return randint(1, self.FIELD_SIZE), randint(1, self.FIELD_SIZE)

    def get_point(self, coordinates):
        if 1 <= coordinates[0] <= self.FIELD_SIZE:
            if 1 <= coordinates[1] <= self.FIELD_SIZE:
                return self.points[(coordinates[0] - 1) * self.FIELD_SIZE + coordinates[1] - 1]
        return None

    def shoot(self, shoot_point):
        miss_shot = False
        all_ships_destroyed = False
        point = self.get_point(shoot_point)
        if point.state == PointType.EMPTY:
            point.change_state(PointType.MISS)
            GameLogger.add_shoot_message("Увы, промах!")
            miss_shot = True
        elif point.state == PointType.SHIP:
            point.change_state(PointType.SHOT)
            if point.ship.destroyed:
                GameLogger.add_shoot_message("Ура! Корабль уничтожен!")
                all_ships_destroyed = self.is_all_ships_destroyed()
            else:
                GameLogger.add_shoot_message("Попадание! Ходите ещё!")
        elif point.state == PointType.MISS or point.state == PointType.SHOT:
            raise DuplicationError()
        return all_ships_destroyed, miss_shot

    def show(self, other):
        between = ' ' * 20
        print(f"{other.caption}{between}{self.caption}")
        print()
        table_header = f"    | {' | '.join(map(str, list(range(1, Desk.FIELD_SIZE + 1))))} |"
        print(f"{table_header}{between}{table_header}")
        hor_sep_line = f"  ---{'----' * Desk.FIELD_SIZE}"
        print(f"{hor_sep_line}{between}{hor_sep_line}")
        for i in range(Desk.FIELD_SIZE):
            map_value = map(
                lambda x: x.state.value,
                other.points[(i * Desk.FIELD_SIZE): (i + 1) * Desk.FIELD_SIZE])
            map_value2 = map(
                lambda x: " " if x.state == PointType.SHIP else x.state.value,
                self.points[(i * Desk.FIELD_SIZE): (i + 1) * Desk.FIELD_SIZE])
            print(f"  {i + 1} | {' | '.join(map_value)} |{between}  {i + 1} | {' | '.join(map_value2)} |")
            if i < Desk.FIELD_SIZE - 1:
                print(f"{hor_sep_line}{between}{hor_sep_line}")
        print()

    # def show(self):
    #     print(f"{self.caption}")
    #     print()
    #     print(f"    | {' | '.join(map(str, list(range(1, Desk.FIELD_SIZE + 1))))} |")
    #     hor_sep_line = f"  ---{'----' * Desk.FIELD_SIZE}"
    #     print(f"{hor_sep_line}")
    #     for i in range(Desk.FIELD_SIZE):
    #         map_value = map(
    #             lambda x: x.state.value, self.points[(i * Desk.FIELD_SIZE): (i + 1) * Desk.FIELD_SIZE])
    #         print(f"  {i + 1} | {' | '.join(map_value)} |")
    #         if i < Desk.FIELD_SIZE - 1:
    #             print(f"{hor_sep_line}")
    #     print()

    # def get_all_neighbours(self, point):
    #     neighbours = list()
    #     for i in range(-1, 2):
    #         if i == 0:
    #             continue
    #         neighbor = self.get_point((point.x - i, point.y))
    #         if neighbor is not None:
    #             neighbours.append(neighbor)
    #
    #     for i in range(-1, 2):
    #         if i == 0:
    #             continue
    #         neighbor = self.get_point((point.x, point.y - i))
    #         if neighbor is not None:
    #             neighbours.append(neighbor)
    #
    #     return neighbours
