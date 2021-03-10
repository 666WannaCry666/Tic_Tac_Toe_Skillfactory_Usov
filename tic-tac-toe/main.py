print("Игра \"Крестики-нолики\" \n")

game_field = [[' ', '1', '2', '3'],
              ['1', ' ', ' ', ' '],
              ['2', ' ', ' ', ' '],
              ['3', ' ', ' ', ' ']]


def print_field():  # функция для печати игрового поля
    print(" ".join(game_field[0]))
    print(" ".join(game_field[1]))
    print(" ".join(game_field[2]))
    print(" ".join(game_field[3]))


def end_game_conditions(cnt):  # функция для проверки условий конца игры
    if cnt == 9:
        return False
    elif game_field[1][1] == 'x' and game_field[1][2] == 'x' and game_field[1][3] == 'x' \
    or game_field[2][1] == 'x' and game_field[2][2] == 'x' and game_field[2][3] == 'x' \
    or game_field[3][1] == 'x' and game_field[3][2] == 'x' and game_field[3][3] == 'x' \
    or game_field[1][1] == 'x' and game_field[2][1] == 'x' and game_field[3][1] == 'x' \
    or game_field[1][2] == 'x' and game_field[2][2] == 'x' and game_field[3][2] == 'x' \
    or game_field[1][3] == 'x' and game_field[2][3] == 'x' and game_field[3][3] == 'x' \
    or game_field[1][1] == 'x' and game_field[2][2] == 'x' and game_field[3][3] == 'x' \
    or game_field[1][3] == 'x' and game_field[2][2] == 'x' and game_field[3][1] == 'x':
        return 'x'
    elif game_field[1][1] == 'o' and game_field[1][2] == 'o' and game_field[1][3] == 'o' \
    or game_field[2][1] == 'o' and game_field[2][2] == 'o' and game_field[2][3] == 'o' \
    or game_field[3][1] == 'o' and game_field[3][2] == 'o' and game_field[3][3] == 'o' \
    or game_field[1][1] == 'o' and game_field[2][1] == 'o' and game_field[3][1] == 'o' \
    or game_field[1][2] == 'o' and game_field[2][2] == 'o' and game_field[3][2] == 'o' \
    or game_field[1][3] == 'o' and game_field[2][3] == 'o' and game_field[3][3] == 'o' \
    or game_field[1][1] == 'o' and game_field[2][2] == 'o' and game_field[3][3] == 'o' \
    or game_field[1][3] == 'o' and game_field[2][2] == 'o' and game_field[3][1] == 'o':
        return 'o'
    else:
        return True


def game(L):
    player = 0
    count = 0
    print_field()
    while True:
        if player == 0:
            print(f"Ход игрока {L[0]}")
            update_field = input("Введите адрес ячейки через пробел, в которую хотите поставить крестик (1-ая цифра - строка): ")
            update_field = list(map(int, update_field.split()))
            if len(update_field) != 2:
                print("Вводить нужно две цифры. 1-ая - номер строки, 2-ая - номер колонки")
                continue
            if game_field[update_field[0]][update_field[1]] == 'x' \
            or game_field[update_field[0]][update_field[1]] == 'o':
                print("Ячейка уже занята")
                print_field()
                continue
            game_field[update_field[0]][update_field[1]] = 'x'
            print_field()
            player = 1
            count += 1
        elif player == 1:
            print(f"Ход игрока {L[1]}")
            update_field = input("Введите адрес ячейки через пробел, в которую хотите поставить нолик (1-ая цифра - строка): ")
            update_field = list(map(int, update_field.split()))
            if len(update_field) != 2:
                print("Вводить нужно две цифры. 1-ая - номер строки, 2-ая - номер колонки")
                continue
            if game_field[update_field[0]][update_field[1]] == 'x' \
            or game_field[update_field[0]][update_field[1]] == 'o':
                print("Ячейка уже занята")
                print_field()
                continue
            game_field[update_field[0]][update_field[1]] = 'o'
            print_field()
            player = 0
            count += 1
        if not end_game_conditions(count):
            print("Игра окончилась ничьей")
            break
        elif end_game_conditions(count) == 'x':
            print(f"Победил игрок {names_list[0]}")
            break
        elif end_game_conditions(count) == 'o':
            print(f"Победил игрок {names_list[1]}")
            break


names_list = [input("Введите имя игрока, ставящего крестики: "), input("Введите имя игрока, ставящего нолики: ")]
game(names_list)

while True:
    end = input("Введите \"Y\", чтобы продолжить игру, или \"N\", чтобы закончить работу программы: ")
    if end == 'Y':
        game_field = [[' ', '1', '2', '3'],
                      ['1', ' ', ' ', ' '],
                      ['2', ' ', ' ', ' '],
                      ['3', ' ', ' ', ' ']]
        game(names_list)
    elif end == 'N':
        print("Работа программы завершена")
        break
    else:
        print("Введен неверный символ!")
        continue
