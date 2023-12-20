field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
count = 0

def print_rules():
    print('Игра "Крестики-нолики"')
    print("")
    print("    Правила игры:     ")
    print("Игрок №1 играет за Х.")
    print("Игрок №2 играет за 0.")
    print("Для отображения символа введите координаты ячейки")
    print("в формате x y, где x - номер строки,")
    print("а y - номер столбца.")
    print("За 1 ход игрок может указать координаты только")
    print("одной ячейки.")
    print("")
    print("Выигрывает тот, кто заполнит своими символами")
    print("всю строчку, столбец или диагональ.")
    print("")


def print_field():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        field_row = f"  {i} | {' | '.join(row)} | "
        print(field_row)
        print("  --------------- ")
    print()


def turn():
    while True:
        coords = input("Твой ход: ").split()

        if len(coords) != 2:
            print("Введи координаты x и y через пробел.")
            continue

        x_coord, y_coord = coords

        if not (x_coord.isdigit()) or not (y_coord.isdigit()):
            print("Введи цифры.")
            continue

        x_coord, y_coord = int(x_coord), int(y_coord)

        if 0 > x_coord or x_coord > 2 or 0 > y_coord or y_coord > 2:
            print("Ой! Ты промахнулся, поле только 3Х3.")
            continue

        if field[x_coord][y_coord] != " ":
            print("Клетка уже занята, выбери другую!")
            continue

        return x_coord, y_coord


def win(x_coord, y_coord, s):
    return ((field[x_coord][0] == field[x_coord][1] == field[x_coord][2] == s) or
            (field[0][y_coord] == field[1][y_coord] == field[2][y_coord] == s) or
            (field[0][0] == field[1][1] == field[2][2] == s) or
            (field[0][2] == field[1][1] == field[2][0] == s))


print_rules()
while True:
    print_field()

    count += 1
    if count % 2 == 1:
        symbol = "X"
        team = "крестики"
    else:
        symbol = "0"
        team = "нолики"
    print(f"Ходят {team}")

    x, y = turn()

    field[x][y] = symbol
    if win(x, y, symbol):
        print_field()
        print(f"Выиграли {team}!")
        break

    if count == 9:
        print("Ничья!")
        break
