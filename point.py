from point_type import PointType


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._state = PointType.EMPTY
        self._ship = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Point: {self.x, self.y}'

    @property
    def state(self):
        return self._state

    @property
    def ship(self):
        return self._ship

    def change_state(self, new_state):
        self._state = new_state

    def link_to_ship(self, ship):
        self._ship = ship

#    @state.setter
#    def state(self, value):
#        self._state = value
