#!/usr/bin/env python3

import os
from termcolor import colored


def clear():
    os.system('clear')


def make_it_yellow(anystring):
    anystring = colored(anystring, "yellow", attrs=["bold"])
    return anystring


def get_index_dict():
    index_dict = {}
    for x in range(81):
        row = x // 9
        column = x % 9
        box = 3 * (row // 3) + column // 3
        index_dict[x] = [row, column, box]
    return index_dict


def print_grid(rows_default, rows):

    rows_printed = list(rows)
    box_border = make_it_yellow("-" * 37)
    line_border = make_it_yellow(":")
    for i in range(3):
        line_border += "-" * 11 + make_it_yellow(":")

    print(box_border + " " * 12 + box_border)
    for i, row in enumerate(rows_printed):
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


def check_win(grid, *args):
    win = True
    if not grid.count(" "):
        for i in range(1, 10):
            for arg in args:
                for sequence in arg:
                    if sequence.count(str(i)) > 1:
                        win = False
                        print("elbasztad")
        if win:
            print("nyertél köcsög")


clear()

# rows_default = generate_grid()
# print_grid(rows_default, rows_default)

grid_default = generate_grid()
grid_solved = generate_grid("test_grid_solved.txt")

rows_default = get_rows(grid_default)
rows_solved = get_rows(grid_solved)

columns_solved = get_columns(grid_solved)
boxes_solved = get_boxes(grid_solved)

print_grid(rows_default, rows_solved)

check_win(grid_solved, rows_solved, columns_solved, boxes_solved)
