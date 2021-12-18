class InfinityLoopError(Exception):
    def __str__(self):
        return "Не удалось найти свободной точки на поле!"
