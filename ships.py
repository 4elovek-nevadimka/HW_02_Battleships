from random import choice

from custom_exceptions.infinity_loop_exception import InfinityLoopError
from ship import Ship


class Ships:

    def __init__(self, desk):
        self.desk = desk
        self.ships = list()
        self.generate_ships()

    def is_all_ships_destroyed(self):
        return all([s.destroyed for s in self.ships])

    def generate_ships(self):
        try:
            ships_list = ((3, 1), (2, 2), (1, 4))
            for pair in ships_list:
                for _ in range(pair[1]):
                    self.generate_ship(pair[0])
        except InfinityLoopError:
            # периодически можно поймать
            self.ships.clear()
            self.desk.reset_points()
            self.generate_ships()

    def generate_ship(self, size):
        self.ships.append(Ship(self.generate_ship_coordinates(size, choice([True, False]))))

    def generate_ship_coordinates(self, size, hor):
        if size == 1:
            return [self.desk.get_first_point()]
        else:
            points = list()
            point = None
            counter = 0
            while len(points) < size:
                counter += 1
                if counter > 100:
                    raise InfinityLoopError("Не удалось построить корабль!")
                if len(points) == 0:
                    point = self.desk.get_first_point()
                    points.append(point)
                else:
                    next_point = self.desk.get_next_point(point, hor)
                    if next_point is not None:
                        if next_point.is_all_neighbours_free:
                            point = next_point
                            points.append(point)
                        else:
                            points.clear()
                    else:
                        points.clear()
            return points
