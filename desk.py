from random import randint
from point import Point
from ships import Ships


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

    def get_first_point(self):
        counter = 0
        while True:
            counter += 1
            if counter > 100:
                raise TimeoutError("Не удалось найти свободной точки на поле!")
            point = self.get_random_point()
            if point.free:
                if point.is_all_neighbours_free:
                    return point

    def get_next_point(self, prev_point, hor):
        if hor:
            return self.get_point((prev_point.x, prev_point.y + 1))
        return self.get_point((prev_point.x + 1, prev_point.y))

    def get_all_neighbours(self, point):
        neighbours = list()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor = self.get_point((point.x - i, point.y - j))
                if neighbor is not None:
                    neighbours.append(neighbor)
        return neighbours

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
