class Player:

    def __init__(self, name, desk):
        self._name = name
        self._desk = desk

    def __eq__(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self._name

    @property
    def desk(self):
        return self._desk
