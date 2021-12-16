from random import choice
from ship import Ship


class Ships:

    def __init__(self, desk):
        self.desk = desk
        self.ships = list()
        self.generate_ships()

    def is_all_ships_destroyed(self):
        return all([s.destroyed for s in self.ships])

    def generate_ships(self):
        self.generate_ship(3)
        self.generate_ship(2)
        self.generate_ship(2)
        self.generate_ship(1)
        self.generate_ship(1)
        self.generate_ship(1)
        self.generate_ship(1)

    def generate_ship(self, size):
        points = self.generate_ship_coordinates(size, choice([True, False]))
        if points is not None:
            self.ships.append(Ship(points))

    def generate_ship_coordinates(self, size, hor):
        if size == 1:
            point = self.desk.get_first_point()
            if point is not None:
                return [point]
            else:
                return None
        else:
            points = list()
            point = None
            counter = 0
            while len(points) < size:
                counter += 1
                if counter > 100:
                    return None
                if len(points) == 0:
                    point = self.desk.get_first_point()
                    if point is None:
                        continue
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
