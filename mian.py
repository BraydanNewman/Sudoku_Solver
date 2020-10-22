import tkinter as tk

class GUI:
    def __init__(self, master):
        self.table = [ ]
        self.number_table = [ ]
        for i in range(0, 9):
            cols = [ ]
            for j in range(0, 9):
                e = tk.Entry(master, width=5, font=60)
                e.grid(row=i, column=j)
                cols.append(e)
            self.table.append(cols)
        self.text = tk.StringVar()
        self.text.set("")
        self.solve_b = tk.Button(master, text="Solve", command=setup, bg='black', fg='white').grid(row=9, column=0, columnspan=9, sticky=tk.NSEW)
        self.clear_b = tk.Button(master, text="Clear", command=self.clear, bg='black', fg='white').grid(row=10, column=0, columnspan=9, sticky=tk.NSEW)
        self.label = tk.Label(master, textvariable=self.text).grid(row=11, column=0, columnspan=9, sticky=tk.NSEW)

    def extract_numbers(self):
        self.number_table.clear()
        for _rows in self.table:
            temp = []
            for _item in _rows:
                number = _item.get()
                if number != "":
                    number = int(_item.get())
                temp.append(number)
            self.number_table.append(temp)

    def label_text(self, text):
        self.text.set(text)

    def draw_board(self, y, x):
        self.table[ y ][ x ].delete(0, "end")
        self.table[ y ][ x ].insert(0, self.number_table[ y ][ x ])

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.table[ i ][ j ].delete(0, "end")
        self.label_text("Cleared")


def full_check(y, x):
    if row_check(y) and column_check(x) and square_check(x, y):
        return True
    else:
        return False


def row_check(y):
    temp_list = [j for j in app.number_table[y] if j != '']
    if len(temp_list) == len(set(temp_list)):
        check = True
    else:
        check = False
    return check


def column_check(x):
    column = []
    for j in range(9):
        column.append(app.number_table[j][x])
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
            temp = app.number_table[y_cord + j][x_cord + f]
            square.append(temp)
    temp_list = [a for a in square if a != '']
    if len(temp_list) == len(set(temp_list)):
        check = True
    else:
        check = False
    return check


def setup():
    app.extract_numbers()
    init_check = True
    for i in range(9):
        for j in range(9):
            if not full_check(i, j):
                init_check = False
    if init_check:
        static_table = [ ]
        for rows in app.number_table:
            static_table_row = [ ]
            for item in rows:
                static_table_row.append(item)
            static_table.append(static_table_row)
        backtracking(static_table)
    else:
        app.label_text("Unsolvable")


def backtracking(static_table):
    main_check_bool = False
    i = 0
    direction = 0
    while not main_check_bool:
        if static_table[divmod(i, 9)[0]][divmod(i, 9)[1]] == "":
            if app.number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] == "":
                app.number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] = 1
                app.draw_board(divmod(i, 9)[0], divmod(i, 9)[1])
                if full_check(divmod(i, 9)[0], divmod(i, 9)[1]):
                    direction = 1
                    i = i + 1
            else:
                app.number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] = app.number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] + 1
                app.draw_board(divmod(i, 9)[0], divmod(i, 9)[1])
                if app.number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] > 9:
                    app.number_table[divmod(i, 9)[0]][divmod(i, 9)[1]] = ""
                    app.draw_board(divmod(i, 9)[0], divmod(i, 9)[1])
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
            app.label_text("Solved")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("SUDOKO")
    window.iconbitmap('sudoku.ico')
    app = GUI(window)
    tk.mainloop()
