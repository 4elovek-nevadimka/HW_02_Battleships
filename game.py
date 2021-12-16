from desk import Desk
from intro import Intro
from player import Player


def make_a_move(player):
    row = input_data(f"Игрок {player}, сделайте ход. Укажите строку: ")
    col = input_data(f"Теперь укажите столбец: ")
    return row, col


def input_data(message):
    while True:
        try:
            input_value = int(input(message))
            if input_value > Desk.FIELD_SIZE or input_value < 1:
                print(f"Укажите число от 1 до {Desk.FIELD_SIZE}.")
            else:
                return input_value
        except ValueError:
            print(f"Ошибка! Укажите число от 1 до {Desk.FIELD_SIZE}.")


# intro part
Intro.clear_screen()
Intro.welcome_print()
Intro.rules_print()
user_name = Intro.input_user_name()

# init users and desks
bot_desk = Desk(True)
bot = Player("bot", bot_desk)
user_desk = Desk(False)
user = Player(user_name, user_desk)
current_player = user

# start the game loop
while True:
    Intro.clear_screen()
    user_desk.show()
    bot_desk.show()

    # for move_record in moves:
    #     print(move_record)
    # if win_flag:
    #     print(f"\nИгра окончена. Победил игрок '{current_player}'")
    #     break
    # if draw_flag:
    #     print(f"\nИгра окончена. Ничья!")
    #     break

    while True:
        coordinates = make_a_move(current_player)
        # current_player.desk
    #     if template_matrix[move[0]][move[1]] == '':
    #         moves.append(f"Ход номер {move_number}: игрок {current_player} походил {move[0]} : {move[1]}")
    #         template_matrix[move[0]][move[1]] = current_player
    #         if move_number > 4:
    #             matrix = [x[1:4] for x in template_matrix[1:4]]
    #             if calculate(move[0] - 1, move[1] - 1, matrix, current_player):
    #                 win_flag = True
    #                 break
    #         if move_number == 9:
    #             draw_flag = True
    #             break
    #         current_player = switch_player(current_player)
    #         move_number += 1
    #         break
    #     else:
    #         print("В указанном поле уже есть значение! Попробуйте ещё раз :)")
