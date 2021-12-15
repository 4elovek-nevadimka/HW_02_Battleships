class Ship:

    def __init__(self, points):
        self._points = []
        self._points.extend(points)
        for point in points:
            # set filled square
            point.set_as_ship()
