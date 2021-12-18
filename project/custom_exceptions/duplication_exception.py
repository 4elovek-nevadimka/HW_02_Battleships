class DuplicationError(Exception):
    def __str__(self):
        return "Ошибка! Нельзя стрелять в одну и ту же клетку несколько раз!\nПопробуйте ещё раз :)"
