import os
#!/usr/bin/env python3

from termcolor import colored


def clear():
    os.system('clear')


def print_grid(rows_file):
    border_line = "-" * 37
    print(colored(border_line, "yellow", attrs=["bold"]))
    for j, num_row in enumerate(rows_file):
        row_list = []
        for num in num_row:
            if num == "0":
                row_list.append(" ")
            else:
                row_list.append(num)
        row = colored("|", "yellow", attrs=["bold"])
        for i, cell in enumerate(row_list):
            cell = colored(cell, "cyan", attrs=["bold"])
            if i % 3 == 2:
                row += f" {cell} " + colored("|", "yellow", attrs=["bold"])
            else:
                row += f" {cell} |"
        print(row)
        if j % 3 == 2:
            print(colored(border_line, "yellow", attrs=["bold"]))
        else:
            print(border_line)


clear()

index_dict = {}

for x in range (81):
    row = x // 9
    column = x % 9
    box = 3 * (row // 3) + column // 3
    index_dict[x] = [row, column, box]

with open("test_grid.txt", "r") as grid_file:
    rows_file = []
    for line in grid_file.read().splitlines():
        rows_file.append(line)

print_grid(rows_file)
