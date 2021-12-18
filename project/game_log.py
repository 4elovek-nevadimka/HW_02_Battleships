class GameLogger:

    move_number = 1
    shoot_message = ""
    moves_log = list()

    @staticmethod
    def add_shoot_message(shoot_message):
        GameLogger.shoot_message = shoot_message

    @staticmethod
    def add_move_message(move_message):
        GameLogger.moves_log.append(f"Ход номер {GameLogger.move_number}: "
                                    f"{move_message} {GameLogger.shoot_message}")
        GameLogger.move_number += 1

    @staticmethod
    def print_log():
        for move_record in GameLogger.moves_log:
            print(move_record)
