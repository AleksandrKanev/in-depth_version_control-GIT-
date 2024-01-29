#   Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.
#   Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске, в
# которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на одной
# вертикали, горизонтали или диагонали.
#   Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

import task_2
from random import randint


def board_list():
    boards = []
    count_board = 1
    while count_board < 5:
        board = []
        count_queens = 1
        count_reset = 0
        while count_queens < 9:
            if count_reset > 2**8:
                board = []
                count_reset = 0
                count_queens = 1
            board.append(tuple(randint(1, 8) for i in range(2)))
            if task_2.check_queens(board):
                count_queens += 1
            else:
                board.pop()
                count_reset += 1
        count_board += 1
        boards.append(board)
        print(boards)

    return boards


print(len(board_list()))


print('Привет, мир!')