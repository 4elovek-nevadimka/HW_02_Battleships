from point import Point


class Desk:
    FIELD_SIZE = 6
    points = []
    ships = []

    def __init__(self):
        for i in range(self.FIELD_SIZE):
            for j in range(self.FIELD_SIZE):
                self.points.append(Point(i + 1, j + 1))

    def add_ship(self, size):
        # ship = Ship
        pass

    def show(self):
        print("\u25A0")
        print(f"    | {' | '.join(map(str, list(range(1, self.FIELD_SIZE + 1))))} |")
        print(f"  ---{'----' * self.FIELD_SIZE}")
        for i in range(self.FIELD_SIZE):
            map_value = map(lambda x: x.state, self.points[(i * self.FIELD_SIZE): (i + 1) * self.FIELD_SIZE])
            row_str = f"  {i + 1} | {' | '.join(map_value)} | "
            print(row_str)
            if i < self.FIELD_SIZE - 1:
                print(f"  ---{'----' * self.FIELD_SIZE}")
        print()
