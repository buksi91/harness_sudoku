#!/usr/bin/env python3

import os
from termcolor import colored


def main():

    clear()

    grid_default = generate_grid()
    grid = list(grid_default)

    rows_default = get_rows(grid_default)
    rows = list(rows_default)

    boxes = get_boxes(grid)

    print_grid(rows_default, rows)

    while True:

        asd = input("Enter something, you filthy animal: ")
        step_data = [6, 8, 4]
        grid = get_grid(step_data, boxes, grid, grid_default)
        rows = get_rows(grid)
        boxes = get_boxes(grid)
        clear()
        print_grid(rows_default, rows)
        if not grid.count(" "):
            columns = get_columns(grid)
            win_status = check_win(rows, columns, boxes)
            if win_status:
                break


def clear():
    os.system('clear')


def make_it_yellow(anystring):
    anystring = colored(anystring, "yellow", attrs=["bold"])
    return anystring


def print_grid(rows_default, rows):

    rows_to_print = list(rows)
    box_border = make_it_yellow("-" * 37)
    line_border = make_it_yellow(":")
    for i in range(3):
        line_border += "-" * 11 + make_it_yellow(":")

    print(box_border + " " * 12 + box_border)
    for i, row in enumerate(rows_to_print):
        row_printed = make_it_yellow("|")
        for j, cell in enumerate(row):
            if rows_default[i][j] == rows[i][j] and rows_default[i][j] != " ":
                cell = colored(cell, "cyan", attrs=["bold"])
            if j % 3 == 2:
                row_printed += f" {cell} " + make_it_yellow("|")
            else:
                row_printed += f" {cell} |"
        if i % 3 == 1:
            row_printed += " " * 12 + make_it_yellow("|")
            for k in range(i, i + 3):
                row_printed += str(k).center(11) + make_it_yellow("|")
        else:
            row_printed += " " * 12 + make_it_yellow("|")
            for k in range(3):
                row_printed += " " * 11 + make_it_yellow("|")
        print(row_printed)
        if i % 3 == 2:
            print(box_border + " " * 12 + box_border)
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
    rows = []
    for i in range(0, 73, 9):
        row = []
        for j in range(i, i + 9):
            row.append(grid[j])
        rows.append(row)
    return rows


def get_columns(grid):
    columns = []
    for i in range(9):
        column = []
        for j in range(i, i + 73, 9):
            column.append(grid[j])
        columns.append(column)
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


def get_index(box_num, box_index):
    index = 27 * ((box_num - 1) // 3) + ((box_num - 1) % 3) * 3 + ((box_index - 1) // 3) * 9 + ((box_index - 1) % 3)
    return index


def get_grid(step_data, boxes, grid, grid_default):
    box_num = step_data[0]
    box_index = step_data[1]
    index = get_index(box_num, box_index)
    if grid_default[index] == " ":
        num = step_data[2]
        grid[index] = num
    return grid


def check_win(*args):
    win_status = True
    for i in range(1, 10):
        for arg in args:
            for sequence in arg:
                if sequence.count(str(i)) > 1:
                    win_status = False
    if win_status:
        print("ebin")
    else:
        print("rekt")
    return win_status


main()
