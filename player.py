class Player:

    def __init__(self, name, desk, bot):
        self._name = name
        self._desk = desk
        self._bot = bot

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
