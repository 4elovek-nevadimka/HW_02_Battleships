from os import system, name


class Intro:

    @staticmethod
    def clear_screen():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    @staticmethod
    def welcome_print():
        print("-----------------------------------------")
        print("  Добро пожаловать в игру 'Морской бой'  ")
        print("-----------------------------------------")

    @staticmethod
    def rules_print():
        print("Правила игры:  ")
        print(" Игроки поочередно стреляют по вражеским ")
        print(" кораблям, указывая координаты точек поля")
        print(" Побеждает тот игрок, кто быстрее уничто-")
        print(" жит все корабли противника.")
        print()

    @staticmethod
    def input_user_name():
        while True:
            try:
                user_name = str(input("Для продолжения введите своё имя: "))
                return user_name
            except ValueError:
                print("Какое-то неправильное имя. Попробуйте ещё раз :)")
