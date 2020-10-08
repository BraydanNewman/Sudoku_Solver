from tkinter import *

window = Tk()
window.title("SUDOKO")
table = []
number_table = []


def make_board():
    for i in range(0, 9):
        cols = []
        for j in range(0, 9):
            e = Entry(window, width=5, font=60)
            e.grid(row=i, column=j)
            cols.append(e)
        table.append(cols)
    solve_b = Button(window, text="Solve", command=backtracking)
    solve_b.grid(row=9, column=0, columnspan=9, sticky=NSEW)
    clear_b = Button(window, text="Clear", command=clear)
    clear_b.grid(row=10, column=0, columnspan=9, sticky=NSEW)


def backtracking():
    def full_check(y, x):
        if row_check(y) and column_check(x) and square_check(x, y):
            return True
        else:
            return False

    def row_check(y):
        temp_list = [j for j in number_table[y] if j != '']
        if len(temp_list) == len(set(temp_list)):
            check = True
        else:
            check = False
        return check

    def column_check(x):
        column = []
        for j in range(9):
            column.append(number_table[j][x])
        temp_list = [j for j in column if j != '']
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

        for f in range(3):
            for j in range(3):
                temp = number_table[y_cord + j][x_cord + f]
                square.append(temp)
        temp_list = [a for a in square if a != '']
        if len(temp_list) == len(set(temp_list)):
            check = True
        else:
            check = False
        return check

    def extract_numbers():
        number_table.clear()
        for _rows in table:
            temp = []
            for _item in _rows:
                number = _item.get()
                if number != "":
                    number = int(_item.get())
                temp.append(number)
            number_table.append(temp)

    extract_numbers()
    static_table = []
    for rows in number_table:
        static_table_row = []
        for item in rows:
            static_table_row.append(item)
        static_table.append(static_table_row)
    main_check_bool = False
    i = 0
    direction = 0
    while not main_check_bool:
        if static_table[divmod(i, 9)[0]][divmod(i, 9)[1]] == "":
            if number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] == "":
                number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] = 1
                draw_board(divmod(i, 9)[0], divmod(i, 9)[1])
                if full_check(divmod(i, 9)[0], divmod(i, 9)[1]):
                    direction = 1
                    i = i + 1
            else:
                number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] = number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] + 1
                draw_board(divmod(i, 9)[0], divmod(i, 9)[1])
                if number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] > 9:
                    number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] = ""
                    draw_board(divmod(i, 9)[0], divmod(i, 9)[1])
                    direction = -1
                    i = i - 1
                else:
                    if full_check(divmod(i, 9)[0], divmod(i, 9)[1]):
                        direction = 1
                        i = i + 1
        else:
            if direction < 0:
                i = i - 1
            elif direction > 0:
                i = i + 1
        if i == 81:
            main_check_bool = True


def draw_board(y, x):
    table[y][x].delete(0, "end")
    table[y][x].insert(0, number_table[y][x])


def clear():
    for i in range(9):
        for j in range(9):
            table[i][j].delete(0, "end")


if __name__ == "__main__":
    make_board()
    window.mainloop()
