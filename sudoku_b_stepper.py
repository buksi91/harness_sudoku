#!/usr/bin/env python3

import os
from termcolor import colored


def main():

    clear()

    grid_default = generate_grid()
    # grid_default = generate_grid("test_grid_solved.txt")
    # grid_default = generate_grid("test_grid_failed.txt")
    grid = list(grid_default)

    rows_default = get_rows(grid_default)
    rows = list(rows_default)

    active_cell = 0

    print_grid(rows_default, rows, active_cell)

    while True:
        step = step_or_fill(rows_default, rows, active_cell)
        if not step.isdigit():
            active_cell = make_step(active_cell, step, grid, rows_default, rows)
        elif grid[active_cell] == " " or (grid[active_cell] != " " and grid[active_cell] != grid_default[active_cell]):
            if step != "0":
                grid[active_cell] = step
            else:
                grid[active_cell] = " "
            rows = get_rows(grid)
            clear()
            print_grid(rows_default, rows, active_cell)
            if not grid.count(" "):
                columns = get_columns(grid)
                boxes = get_boxes(grid)
                win_status = check_win(rows, columns, boxes)
                if win_status:
                    break
        else:
            clear()
            print_grid(rows_default, rows, active_cell)


def clear():
    os.system('clear')


def color_box_border(anystring):
    anystring = colored(anystring, "white", attrs=["bold"])
    return anystring


def color_default_numbers(anystring):
    anystring = colored(anystring, "white", attrs=["bold"])
    return anystring


def color_active_default_numbers(anystring):
    anystring = colored(anystring, "white", attrs=["reverse", "bold"])
    return anystring


def color_input_numbers(anystring):
    anystring = colored(anystring, "green", attrs=["bold"])
    return anystring


def color_active_input_numbers(anystring):
    anystring = colored(anystring, "green", attrs=["reverse", "bold"])
    return anystring


def color_active_empty_cell(anystring):
    anystring = colored(anystring, "green", attrs=["reverse", "bold"])
    return anystring


def print_grid(rows_default, rows, active_cell):

    rows_to_print = list(rows)
    box_border = color_box_border("-" * 37)
    line_border = color_box_border(":")
    for i in range(3):
        line_border += "-" * 11 + color_box_border(":")

    print(box_border)
    for i, row in enumerate(rows_to_print):
        row_printed = color_box_border("|")
        for j, cell in enumerate(row):

            if rows_default[i][j] == rows[i][j] and rows_default[i][j] != " ":
                if 9 * i + j != active_cell:
                    cell = color_default_numbers(cell)
                else:
                    cell = color_active_default_numbers(cell)
            if rows_default[i][j] != rows[i][j] and rows[i][j] != " ":
                if 9 * i + j != active_cell:
                    cell = color_input_numbers(cell)
                else:
                    cell = color_active_input_numbers(cell)
            if rows[i][j] == " " and 9 * i + j == active_cell:
                cell = color_active_empty_cell(cell)

            if j % 3 == 2:
                row_printed += f" {cell} " + color_box_border("|")
            else:
                row_printed += f" {cell} |"
        print(row_printed)
        if i % 3 == 2:
            if i == 8:
                box_border += "\n"
            print(box_border)
        else:
            print(line_border)


def generate_grid(filename="test_grid.txt"):
    with open(filename, "r") as grid_file:
        rows_file = []
        for line in grid_file.read().splitlines():
            rows_file.append(line)

    grid = []
    for i, num_row in enumerate(rows_file):
        for num in num_row:
            if num == "0":
                grid.append(" ")
            else:
                grid.append(num)
    return grid


def get_rows(grid):
    rows = [[grid[j] for j in range(i, i + 9)] for i in range(0, 73, 9)]
    return rows


def get_columns(grid):
    columns = [[grid[j] for j in range(i, i + 73, 9)] for i in range(9)]
    return columns


def get_boxes(grid):
    boxes = []
    for i in range(0, 73, 27):
        # in every row of boxes
        for j in range(i, i + 9, 3):
            # starting from the first row of the row of boxes
            box = []
            for k in range(j, j + 19, 9):
                # in every box row
                for l in range(k, k + 3):
                    box.append(grid[l])
            boxes.append(box)
    return boxes


def step_or_fill(rows_default, rows, active_cell):
    while True:
        print("Make a step:".rjust(13), "w/a/s/d")
        print("Make 3 steps:".rjust(13), "ww/aa/ss/dd (example: 'ww' - 3 steps up)")
        print("Fill a cell:".rjust(13), "1 - 9")
        print("Clear a cell:".rjust(13), "0\n")
        step = input("Your input: ")
        if step.isdigit() and int(step) in range(0, 10):
            return step
        elif step in "wasd" and len(step) == 1:
            return step
        elif step[0] in "wasd" and step[1] == step[0] and len(step) == 2:
            return step
        else:
            clear()
            print_grid(rows_default, rows, active_cell)


def make_step(active_cell, step, grid, rows_default, rows):
    steps = {
        "w": (lambda c: c - 9), "ww": (lambda c: c - 27),
        "s": (lambda c: c + 9), "ss": (lambda c: c + 27),
        "a": (lambda c: c - 1), "aa": (lambda c: c - 3),
        "d": (lambda c: c + 1), "dd": (lambda c: c + 3)
    }
    active_cell_copy = int(active_cell)
    active_cell = steps[step](active_cell)
    if active_cell in range(81):
        clear()
        print_grid(rows_default, rows, active_cell)
        return active_cell
    active_cell = int(active_cell_copy)
    clear()
    print_grid(rows_default, rows, active_cell)
    return active_cell


def check_win(*args):
    win_status = True
    for i in range(1, 10):
        for arg in args:
            for sequence in arg:
                if sequence.count(str(i)) > 1:
                    win_status = False
    if win_status:
        print("Top noice")
    else:
        print("Some numbers are in the wrong place. Try again!\n")
    return win_status


main()
