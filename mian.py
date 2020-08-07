from tkinter import *
window=Tk()
window.title("SUDOKO")
table = [ ]
number_table = [ ]


def make_board():
    for i in range(0,9):
        cols = []
        for j in range(0,9):
            e = Entry(window, width=5, font=60)
            e.grid(row=i, column=j)
            cols.append(e)
        table.append(cols)
    solve_b = Button(window, text="Solve", command=backtracking)
    solve_b.grid(row=9, column=0, columnspan=9, sticky=NSEW)

def backtracking():
    for rows in table:
        for item  in rows:
            item.config(state=DISABLED)

    def row_check(y):
        if len(number_table[y]) == len(set(number_table[y])):
            check = True
        else:
            check = False
        return check

    def column_check(x):
        column = []
        for i in range(9):
            column.append(number_table[x][i])
        if len(column) == len(set(column)):
            check = True
        else:
            check = False
        return check

    def square_check(x,y):
        square = []
        def quad_check(num):
            if num < 3:
                x_multiplier = 0
            elif num < 6:
                x_multiplier = 1
            else:
                x_multiplier = 2




    def extract_numbers():
        number_table.clear()
        for _rows in table:
            temp = []
            for _item in _rows:
                temp.append(_item.get())
            number_table.append(temp)


make_board()
window.mainloop()