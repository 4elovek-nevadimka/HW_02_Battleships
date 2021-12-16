from point_type import PointType


class Point:

    def __init__(self, x, y, desk):
        self.x, self.y = x, y
        self._state = PointType.EMPTY
        self._ship = None
        self._free = True
        self._neighbours = list()
        self._desk = desk

    @property
    def state(self):
        if not self.free:
            if self.ship is None:
                return PointType.SHOT
        return self._state

    @property
    def ship(self):
        return self._ship

    @property
    def free(self):
        return self._free

    @property
    def neighbours(self):
        if len(self._neighbours) == 0:
            self._neighbours.extend(self._desk.get_all_neighbours(self))
        return self._neighbours

    @property
    def is_all_neighbours_free(self):
        return all([n.free for n in self.neighbours])

    def change_state(self, new_state):
        self._state = new_state

    def link_to_ship(self, ship):
        self._ship = ship
        self._free = False

    def reset(self):
        self._state = PointType.EMPTY
        self._ship = None
        self._free = True
        self._neighbours.clear()

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y
    #
    # def __str__(self):
    #     return f'Point: {self.x, self.y}'

    # @free.setter
    # def free(self, value):
    #     self._free = value

    # @state.setter
    # def state(self, value):
    #     self._state = value
