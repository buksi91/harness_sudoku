#!/usr/bin/env python3

import os
from termcolor import colored


def main():

    clear()

    grid_default = generate_grid()  # "test_grid_solved.txt" "test_grid_failed.txt"
    grid = list(grid_default)
    active_index = 0

    print_grid(grid, grid_default, active_index)

    grid_full = False
    unsolved = True
    while unsolved:

        step = step_or_fill(grid, grid_default, active_index)

        if step.isdigit():
            valid_cell = get_cell_validity(grid, grid_default, active_index)
            if valid_cell:
                grid = get_grid(step, grid, active_index)
                grid_full = check_grid(grid)
        else:
            active_index = get_active_index(step, active_index)

        clear()
        print_grid(grid, grid_default, active_index)

        if grid_full:
            win_status = get_win_status(grid)
            unsolved = get_unsolved(win_status)


def get_cell_validity(grid, grid_default, active_index):
    if grid[active_index] == " ":
        return True
    elif grid[active_index] != grid_default[active_index]:
        return True
    else:
        return False


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


def color_the_cell(cell_value, default_value, cell_index, active_index):
    if cell_value != " ":
        if cell_value == default_value:
            if cell_index == active_index:
                return color_active_default_numbers(cell_value)
            else:
                return color_default_numbers(cell_value)
        else:
            if cell_index == active_index:
                return color_active_input_numbers(cell_value)
            else:
                return color_input_numbers(cell_value)
    elif cell_index == active_index:
        return color_active_empty_cell(cell_value)
    else:
        return cell_value


def print_grid(grid, grid_default, active_index):

    rows = get_rows(grid)

    WIDTH = 37
    rows_to_print = list(rows)
    box_border = color_box_border("-" * WIDTH)
    line_border = color_box_border(":")
    for i in range(3):
        line_border += "-" * 11 + color_box_border(":")

    print(box_border)
    for i, row in enumerate(rows_to_print):
        row_to_print = color_box_border("|")
        for j, cell_value in enumerate(row):
            cell_index = 9 * i + j
            default_value = grid_default[cell_index]
            cell_value = color_the_cell(cell_value, default_value, cell_index, active_index)
            if j % 3 == 2:
                row_to_print += f" {cell_value} " + color_box_border("|")
            else:
                row_to_print += f" {cell_value} |"
        print(row_to_print)
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
    rows = [[grid[9 * i + j] for j in range(9)] for i in range(9)]
    return rows


def get_columns(grid):
    columns = [[grid[i + 9 * j] for j in range(9)] for i in range(9)]
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


def step_or_fill(grid, grid_default, active_index):
    JUST = 13
    while True:
        print("Make a step:".rjust(JUST), "w/a/s/d")
        print("Make 3 steps:".rjust(JUST), "ww/aa/ss/dd (example: 'ww' - 3 steps up)")
        print("Fill a cell:".rjust(JUST), "1 - 9")
        print("Clear a cell:".rjust(JUST), "0\n")
        step = input("Your input: ")
        step_keys = ["w", "a", "s", "d"]
        if step.isdigit() and int(step) in range(0, 10):
            return step
        elif step in step_keys or step in [x * 2 for x in step_keys]:
            return step
        else:
            clear()
            print_grid(grid, grid_default, active_index)


def get_active_index(step, active_index):
    steps = {
        "w": (lambda c: c - 9), "ww": (lambda c: c - 27),
        "s": (lambda c: c + 9), "ss": (lambda c: c + 27),
        "a": (lambda c: c - 1), "aa": (lambda c: c - 3),
        "d": (lambda c: c + 1), "dd": (lambda c: c + 3)
    }
    active_index_copy = int(active_index)
    active_index = steps[step](active_index)
    if active_index not in range(81):
        active_index = int(active_index_copy)
    return active_index


def get_grid(step, grid, active_index):
    if step != "0":
        grid[active_index] = step
    else:
        grid[active_index] = " "
    return grid


def check_grid(grid):
    if grid.count(" "):
        return False
    else:
        return True


def get_win_status(grid):
    rows = get_rows(grid)
    columns = get_columns(grid)
    boxes = get_boxes(grid)
    win_status = True
    for i in range(1, 10):
        for sequence_type in [rows, columns, boxes]:
            for sequence in sequence_type:
                if sequence.count(str(i)) > 1:
                    win_status = False
    return win_status


def get_unsolved(win_status):
    if win_status:
        print("Top noice")
        return False
    else:
        print("Some numbers are in the wrong place. Try again!\n")
        return True


main()
