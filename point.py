class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._state = ' '

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Point: {self.x, self.y}'

    @property
    def state(self):
        return self._state

    def set_as_ship(self):
        self._state = "\u25A0"

#    @state.setter
#    def state(self, value):
#        self._state = value
