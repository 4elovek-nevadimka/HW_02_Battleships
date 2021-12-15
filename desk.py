from point import Point
from ship import Ship


class Desk:
    FIELD_SIZE = 6

    def __init__(self, ai_flag):
        self.points = []
        for i in range(self.FIELD_SIZE):
            for j in range(self.FIELD_SIZE):
                self.points.append(Point(i + 1, j + 1))
        self.ships = []
        self.generate_ships(ai_flag)

    def generate_ships(self, ai_flag):
        if ai_flag:
            self.add_ship(self.points[9: 9 + 3])
            self.add_ship([self.points[0], self.points[1]])
            self.add_ship([self.points[13], self.points[19]])
            self.add_ship([self.points[30]])
            self.add_ship([self.points[23]])
            self.add_ship([self.points[27]])
            self.add_ship([self.points[35]])
        else:
            self.add_ship(self.points[6: 6 + 3])
            self.add_ship([self.points[4], self.points[5]])
            self.add_ship([self.points[23], self.points[29]])
            self.add_ship([self.points[33]])
            self.add_ship([self.points[30]])
            self.add_ship([self.points[18]])
            self.add_ship([self.points[20]])

    def add_ship(self, coordinates):
        ship = Ship(coordinates)
        self.ships.append(ship)

    def show(self):
        print(f"    | {' | '.join(map(str, list(range(1, self.FIELD_SIZE + 1))))} |")
        print(f"  ---{'----' * self.FIELD_SIZE}")
        for i in range(self.FIELD_SIZE):
            map_value = map(lambda x: x.state, self.points[(i * self.FIELD_SIZE): (i + 1) * self.FIELD_SIZE])
            row_str = f"  {i + 1} | {' | '.join(map_value)} | "
            print(row_str)
            if i < self.FIELD_SIZE - 1:
                print(f"  ---{'----' * self.FIELD_SIZE}")
        print()
