#   Добавьте в пакет, созданный на семинаре шахматный модуль.
#   Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens), которая проверяет все
# возможные пары ферзей.
#   Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
#   Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг
# друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.


queens = [(1, 1), (2, 2), (3, 3)]


def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return False
    elif q1[0] > q1[1]:
        for i in range(1, 9):
            if (q1[0] - q1[1] + i == q2[0] or q1[0] + q1[1] - i == q2[0]) and i == q2[1]:
                return False
    elif q1[0] < q1[1]:
        for i in range(1, 9):
            if i == q2[0] and (q1[1] - q1[0] + i == q2[1] or q1[1] + q1[0] - i == q2[1]):
                return False
    elif q1[0] == q1[1]:
        for i in range(1, 9):
            if i == q2[0] and i == q2[1] or q1[0] * 2 - i == q2[0] and i == q2[1]:
                return False
    return True


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(len(queens)):
            if i != j:
                if not is_attacking(queens[i], queens[j]):
                    return False

    return True

if __name__ == '__main__':
    print(check_queens(queens))
