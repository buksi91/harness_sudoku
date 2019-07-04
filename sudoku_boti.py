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

        step_data = get_input(rows_default, rows)
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


def color_box_border(anystring):
    anystring = colored(anystring, "white", attrs=["bold"])
    return anystring


def color_default_number(anystring):
    anystring = colored(anystring, "white", attrs=["bold"])
    return anystring


def color_input_number(anystring):
    anystring = colored(anystring, "green", attrs=["bold"])
    return anystring


def print_grid(rows_default, rows):

    rows_to_print = list(rows)
    box_border = color_box_border("-" * 37)
    line_border = color_box_border(":")
    for i in range(3):
        line_border += "-" * 11 + color_box_border(":")

    print(box_border + " " * 12 + box_border)
    for i, row in enumerate(rows_to_print):
        row_printed = color_box_border("|")
        for j, cell in enumerate(row):
            if rows_default[i][j] == rows[i][j] and rows_default[i][j] != " ":
                cell = color_default_number(cell)
            if rows_default[i][j] != rows[i][j] and rows[i][j] != " ":
                cell = color_input_number(cell)
            if j % 3 == 2:
                row_printed += f" {cell} " + color_box_border("|")
            else:
                row_printed += f" {cell} |"
        if i % 3 == 1:
            row_printed += " " * 12 + color_box_border("|")
            for k in range(i, i + 3):
                row_printed += str(k).center(11) + color_box_border("|")
        else:
            row_printed += " " * 12 + color_box_border("|")
            for k in range(3):
                row_printed += " " * 11 + color_box_border("|")
        print(row_printed)
        if i % 3 == 2:
            print(box_border + " " * 12 + box_border)
        else:
            print(line_border)
    print()


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


def input_check(input, player_moves_list):

    if input.isdigit():
        for x in range(2):
            if input[x] == "0":
                return True
        if len(input) != 3:
            return True
        elif int(input) >= 110 and int(input) <= 999:
            for x in range(3):
                player_moves_list.append(str(input[x]))
            return False
    else:
        return True


def get_input(rows_default, rows):
    player_moves_list = []
    input_loop = True
    while input_loop:
        clear()
        print_grid(rows_default, rows)
        output = ''
        box = input("Please choose a box (1-9): ")
        brancket = input("Please choose a cell (1-9): ")
        number = input("Please enter a number (1-9): ")
        output = str(box)+str(brancket)+str(number)
        player_moves_list = []
        input_loop = input_check(output, player_moves_list)
        print(player_moves_list)
        print(input_loop)
        print("dikmoree")
    return player_moves_list


def get_index(box_num, box_index):
    box_row = (int(box_num) - 1) // 3
    box_column = (int(box_num) - 1) % 3
    row_in_box = (int(box_index) - 1) // 3
    column_in_box = (int(box_index) - 1) % 3
    index = box_row * 27 + box_column * 3 + row_in_box * 9 + column_in_box
    return index


def get_grid(step_data, boxes, grid, grid_default):
    box_num = step_data[0]
    box_index = step_data[1]
    num = step_data[2]
    index = get_index(box_num, box_index)
    if grid_default[index] == " ":
        if num != "0":
            grid[index] = num
        else:
            grid[index] = " "
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
