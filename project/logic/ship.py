from project.logic.point_type import PointType


class Ship:

    def __init__(self, points):
        self._points = []
        self._points.extend(points)
        for point in points:
            point.change_state(PointType.SHIP)
            point.link_to_ship(self)

    @property
    def destroyed(self):
        return all([p.state == PointType.SHOT for p in self._points])
