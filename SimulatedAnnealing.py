import random
import math
from copy import copy
from time import process_time


class Queen:
    def __init__(self, row, column):
        self.row = int(row)
        self.column = int(column)
        self.attackers = 0

    def print(self):
        print("(", self.row, ",", self.column, ")", sep='', end='')

    def __eq__(self, other):
        if self is not None:
            return self.column == other.column and self.row == other.row

    def __sub__(self, other):
        if self is not None:
            return abs(self.column - other.column) - abs(self.row - other.row)


class Board:
    def __init__(self, w):
        if w < 4:
            self.w = 4
            self.h = 4
        else:
            self.w = w
            self.h = w
        self.board = [[0 for x in range(self.w)] for y in range(self.h)]
        self.queens = []

    def print(self):
        for i in self.board:

            for j in range(self.w):
                if isinstance(i[j], Queen):
                    i[j].print()
                else:
                    print("(-", ",", "-)", sep='', end='')
            print()

    def choose_random(self):
        rnd = random.randint(0, self.w - 1)
        for i in self.queens:
            if i.column == rnd:
                x = copy(i)
                return x

    def choose_next(self):
        queens = copy(self.queens)
        q1 = self.choose_random()
        rnd = random.randint(0, self.w - 1)
        q1.row = rnd
        for i, queen in enumerate(queens):
            if queen.column == q1.column:
                queens[i] = q1
                break
        return queens

    def update(self):
        queens = copy(self.queens)
        for i, queen in enumerate(queens):
            for j in range(self.w):
                if isinstance(self.board[j][i], Queen):
                    if self.board[j][i] not in queens:
                        self.board[j][i] = 0
                if j == queen.row:
                    self.board[j][i] = queen


def get_num_of_attackers(queens):
    attackers = 0
    for i in queens:
        row1, row2, adj1, adj2, adj3, adj4 = True, True, True, True, True, True
        for j in queens:
            if i.row == j.row and i.column < j.column and i != j and row1:
                attackers += 1
                row1 = False
            elif i.row == j.row and i.column > j.column and i != j and row2:
                attackers += 1
                row2 = False
            elif i - j == 0 and i.column < j.column and i.row < j.row and i != j and adj1:
                attackers += 1
                adj1 = False
            elif i - j == 0 and i.column > j.column and i.row > j.row and i != j and adj2:
                attackers += 1
                adj2 = False
            elif i - j == 0 and i.column < j.column and i.row > j.row and i != j and adj3:
                attackers += 1
                adj3 = False
            elif i - j == 0 and i.column > j.column and i.row < j.row and i != j and adj4:
                attackers += 1
                adj4 = False
    return attackers


def init(board):
    rand = []

    for i in range(board.w):
        x = random.randint(0, board.w - 1)
        y = i
        str1 = x, y
        while str1 in rand:
            x = random.randint(0, board.w - 1)
            str1 = x, y
        rand.append(str1)
        q1 = Queen(x, y)
        board.board[x][y] = q1
        board.queens.append(q1)


def simulated_annealing(board, temp, alpha):
    min_temp = 0.1
    next_value = 10
    steps_list = []
    prop_list = []
    energy_list = []
    while next_value != 0:
        current_value = get_num_of_attackers(board.queens)
        # print("Current:")
        for k in board.queens:
            k.print()
        qu1 = board.choose_next()
        # print("\nNext:")
        for k in qu1:
            k.print()
        print()
        next_value = get_num_of_attackers(qu1)
        energy = current_value - next_value
        print()
        # print("current =", current_value)
        # print("next =", next_value)
        print("energy =", energy)
        print(temp)
        rand = random.uniform(0, 1)
        prop_func = math.exp(energy / temp)
        prop_list.append(prop_func)
        print("rand:", rand)
        print("prop_func:", prop_func)
        energy_list.append(energy)
        if energy > 0:
            board.queens = qu1
        elif rand < prop_func:
            board.queens = qu1
        board.update()
        steps_list.append(board.queens)
        print("---------------------------------------------------")
        # board.print()
        if temp > min_temp:
            temp = alpha * temp
        if temp < min_temp:
            temp = min_temp
    return steps_list, prop_list, energy_list


def startAnnealing(n, temp, alpha):
    start_time = process_time()
    b1 = Board(n)
    init(b1)
    b1.print()
    steps_list, prop_list, energy_list = simulated_annealing(b1, temp, alpha)
    stop_time = process_time()
    print("Elapsed time:", stop_time - start_time)
    return steps_list, prop_list, energy_list



if __name__ == "__main__":
    startAnnealing(4, 1000, 0.9)








