#!/usr/bin/env python3

import os
from termcolor import colored


def clear():
    os.system('clear')


def make_yellow(anystring):
    anystring = colored(anystring, "yellow", attrs=["bold"])
    return anystring


def print_grid(rows_file):

    box_border = make_yellow("-" * 37)
    line_border = make_yellow(":")
    for i in range(3):
        line_border += "-" * 11 + make_yellow(":")

    print(box_border, " " * 12, )
    for j, num_row in enumerate(rows_file):
        row_list = []
        for num in num_row:
            if num == "0":
                row_list.append(" ")
            else:
                row_list.append(num)
        row = make_yellow("|")
        for i, cell in enumerate(row_list):
            cell = colored(cell, "cyan", attrs=["bold"])
            if i % 3 == 2:
                row += f" {cell} " + make_yellow("|")
            else:
                row += f" {cell} |"
        print(row)
        if j % 3 == 2:
            print(box_border)
        else:
            print(line_border)


clear()

index_dict = {}

for x in range(81):
    row = x // 9
    column = x % 9
    box = 3 * (row // 3) + column // 3
    index_dict[x] = [row, column, box]

with open("test_grid.txt", "r") as grid_file:
    rows_file = []
    for line in grid_file.read().splitlines():
        rows_file.append(line)

print_grid(rows_file)
