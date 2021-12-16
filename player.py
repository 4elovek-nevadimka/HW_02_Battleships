from desk import Desk


class Player:

    def __init__(self, name, bot):
        self._name = name
        self._bot = bot
        if bot:
            self._desk = Desk("Поле противника")
        else:
            self._desk = Desk("Моё игровое поле")

    def __eq__(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self._name

    @property
    def desk(self):
        return self._desk

    @property
    def is_bot(self):
        return self._bot
