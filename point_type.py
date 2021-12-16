from enum import Enum


class PointType(Enum):
    EMPTY = ' '
    SHIP = "\u25A0"
    SHOT = 'X'
    MISS = 'T'
