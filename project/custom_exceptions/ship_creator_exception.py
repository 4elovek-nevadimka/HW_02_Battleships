class ShipCreatorError(Exception):
    def __str__(self):
        return "Не удалось построить корабль!"