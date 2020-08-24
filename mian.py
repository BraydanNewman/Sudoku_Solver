import random
from tkinter import *
import tkinter as tk

window = Tk()
window.title("SUDOKO")
table = []
number_table = []


def make_board():
    for i in range(0, 9):
        cols = []
        for j in range(0, 9):
            enterText = tk.StringVar()
            e = Entry(window, width=5, font=60, textvariable=enterText)
            lol = random.randint(0, 4)
            if lol == 3:
                enterText.set(str(random.randint(1, 9)))
            e.grid(row=i, column=j)
            cols.append(e)
        table.append(cols)
    solve_b = Button(window, text="Solve", command=backtracking)
    solve_b.grid(row=9, column=0, columnspan=9, sticky=NSEW)


def backtracking():
    def full_check(x, y):
        check = 
        if row_check(y):
            return True
        elif

    def row_check(y):
        temp_list = [i for i in number_table[y] if i != '']
        if len(temp_list) == len(set(temp_list)):
            check = True
        else:
            check = False
        return check

    def column_check(x):
        column = []
        for i in range(9):
            column.append(number_table[i][x])
        temp_list = [i for i in column if i != '']
        if len(temp_list) == len(set(temp_list)):
            check = True
        else:
            check = False
        return check

    def square_check(x, y):
        square = []

        def quad_check(num):
            if num < 3:
                x_multiplier = 0
            elif num < 6:
                x_multiplier = 1
            else:
                x_multiplier = 2
            return x_multiplier

        x_cord = quad_check(x) * 3
        y_cord = quad_check(y) * 3

        for i in range(3):
            for j in range(3):
                temp = number_table[y_cord + j][x_cord + i]
                square.append(temp)
        temp_list = [i for i in square if i != '']
        if len(temp_list) == len(set(temp_list)):
            check = True
        else:
            check = False
        return check

    def extract_numbers():
        number_table.clear()
        for _rows in table:
            temp = [ ]
            for _item in _rows:
                temp.append(_item.get())
            number_table.append(temp)

    for rows in table:
        for item in rows:
            item.config(state=DISABLED)

    # False if double
    extract_numbers()
    static_table = number_table

    collision_check = False
    while not collision_check:
        cell_num = 0

        extract_numbers()

        pos_check = divmod(cell_num, 9)
        if static_table[pos_check[0]][pos_check[1]] is None:
            if number_table[pos_check[0]][pos_check[1]] is not None:
                number_table[pos_check[0]][pos_check[1]] = number_table[pos_check[0]][pos_check[1]] + 1
            else:
                number_table[pos_check[0]][pos_check[1]] = 1

        else:
            cell_num = cell_num + 1
        if row_check(pos_check[0]) and column_check(pos_check[1]) and square_check(pos_check[1], pos_check[0]):
            cell_num = cell_num + 1
        else:
            if number_table[pos_check[0]][pos_check[1]] == 9:
                pass
            else:
                number_table[pos_check[0]][pos_check[1]] = number_table[pos_check[0]][pos_check[1]] + 1


if __name__ == "__main__":
    make_board()
    window.mainloop()
