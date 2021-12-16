from desk import Desk
from intro import Intro
from player import Player
from point_type import PointType


def make_a_move(player):
    if player.is_bot:
        return player.desk.get_random_coordinates()
    else:
        row = input_data(f"Игрок {player.name}, сделайте ход. Укажите строку: ")
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


def shoot(enemy, location):
    move_result = ""
    switch_player = False
    all_ships_destroyed = False
    point = enemy.desk.get_point(location)
    if point.state == PointType.EMPTY:
        point.change_state(PointType.MISS)
        move_result = "Увы, промах!"
        switch_player = True
    elif point.state == PointType.SHIP:
        point.change_state(PointType.SHOT)
        if point.ship.destroyed:
            move_result = "Ура! Корабль уничтожен!"
            all_ships_destroyed = enemy.desk.is_all_ships_destroyed()
        else:
            move_result = "Попадание! Ходите ещё!"
    elif point.state == PointType.MISS or point.state == PointType.SHOT:
        raise ValueError("Ошибка! Нельзя стрелять в одну и ту же клетку несколько раз!")
    return all_ships_destroyed, switch_player, move_result


def show_desks(player, enemy):
    between = ' ' * 20
    print(f"{player.desk.caption}{between}{enemy.desk.caption}")
    print()
    table_header = f"    | {' | '.join(map(str, list(range(1, Desk.FIELD_SIZE + 1))))} |"
    print(f"{table_header}{between}{table_header}")
    hor_sep_line = f"  ---{'----' * Desk.FIELD_SIZE}"
    print(f"{hor_sep_line}{between}{hor_sep_line}")
    for i in range(Desk.FIELD_SIZE):
        map_value = map(
            lambda x: x.state.value, player.desk.points[(i * Desk.FIELD_SIZE): (i + 1) * Desk.FIELD_SIZE])
        map_value2 = map(
            lambda x: x.state.value, enemy.desk.points[(i * Desk.FIELD_SIZE): (i + 1) * Desk.FIELD_SIZE])
        print(f"  {i + 1} | {' | '.join(map_value)} |{between}  {i + 1} | {' | '.join(map_value2)} |")
        if i < Desk.FIELD_SIZE - 1:
            print(f"{hor_sep_line}{between}{hor_sep_line}")
    print()


# intro part
Intro.clear_screen()
Intro.welcome_print()
Intro.rules_print()
user_name = Intro.input_user_name()

# init users and desks
current_player = Player(user_name, False)
current_enemy = Player("bot", True)

# move logs
moves = list()
move_number = 1

game_over = False

# start the game loop
while True:
    Intro.clear_screen()
    if not current_player.is_bot:
        show_desks(current_player, current_enemy)
    else:
        show_desks(current_enemy, current_player)
    # print game log
    for move_record in moves:
        print(move_record)
    # exit game condition
    if game_over:
        print(f"\nИгра окончена. Победил игрок '{current_player.name}'")
        break
    # move loop
    while True:
        coordinates = make_a_move(current_player)
        try:
            shoot_result = shoot(current_enemy, coordinates)
            moves.append(
                f"Ход номер {move_number}: игрок {current_player.name} походил {coordinates[0]} : {coordinates[1]}")
            moves.append(shoot_result[2])
            if shoot_result[0]:
                game_over = True
                break
            if shoot_result[1]:
                current_player, current_enemy = current_enemy, current_player
            move_number += 1
            break
        except ValueError as ex:
            print(str(ex))
            print("Попробуйте ещё раз :)")
