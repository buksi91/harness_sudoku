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
            if rows_default[j] == rows[j] and rows_default[j] != " ":
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


def generate_grid():
    with open("test_grid.txt", "r") as grid_file:
        rows_file = []
        for line in grid_file.read().splitlines():
            rows_file.append(line)
    rows = []
    for i, num_row in enumerate(rows_file):
        row = []
        for num in num_row:
            if num == "0":
                row.append(" ")
            else:
                row.append(num)
        rows.append(row)
    return rows


clear()

rows_default = generate_grid()
print_grid(rows_default, rows_default)
