from enum import Enum


class PointType(Enum):
    # пустая клетка
    EMPTY = ' '
    # клетка - корабль
    SHIP = "\u25A0"
    # попал
    SHOT = 'X'
    # промах
    MISS = 'T'
