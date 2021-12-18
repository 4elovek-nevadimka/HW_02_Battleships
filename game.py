from project.intro import Intro
from project.game_log import GameLogger
from project.players.ai_bot import AiBot
from project.players.user import User


def start():
    Intro.clear_screen()
    Intro.welcome_print()
    Intro.rules_print()
    user_name = Intro.input_user_name()
    # init users
    user = User(user_name)
    ai_bot = AiBot("bot")
    # start game loop
    loop(user, ai_bot)


def loop(user, ai_bot):
    while True:
        Intro.clear_screen()
        user.enemy_desk.show(ai_bot.enemy_desk)
        GameLogger.print_log()
        # make a move for user
        if user.make_a_move(ai_bot.enemy_desk):
            break
        # make a move for bot
        if ai_bot.make_a_move(user.enemy_desk):
            break


start()

# def show_desks(self):
#     between = ' ' * 20
#     print(f"{self.user_desk.caption}{between}{self.bot_desk.caption}")
#     print()
#     table_header = f"    | {' | '.join(map(str, list(range(1, Desk.FIELD_SIZE + 1))))} |"
#     print(f"{table_header}{between}{table_header}")
#     hor_sep_line = f"  ---{'----' * Desk.FIELD_SIZE}"
#     print(f"{hor_sep_line}{between}{hor_sep_line}")
#     for i in range(Desk.FIELD_SIZE):
#         map_value = map(
#             lambda x: x.state.value,
#             self.user_desk.points[(i * Desk.FIELD_SIZE): (i + 1) * Desk.FIELD_SIZE])
#         map_value2 = map(
#             # small cheat ^) -->
#             # lambda x: "" if x.state == PointType.SHIP else x.state.value,
#             # big cheat -->
#             # lambda x: x.state.value, enemy.desk.points[(i * Desk.FIELD_SIZE): (i + 1) * Desk.FIELD_SIZE])
#             lambda x: " " if x.state == PointType.SHIP else x.state.value,
#             self.bot_desk.points[(i * Desk.FIELD_SIZE): (i + 1) * Desk.FIELD_SIZE])
#         print(f"  {i + 1} | {' | '.join(map_value)} |{between}  {i + 1} | {' | '.join(map_value2)} |")
#         if i < Desk.FIELD_SIZE - 1:
#             print(f"{hor_sep_line}{between}{hor_sep_line}")
#     print()
