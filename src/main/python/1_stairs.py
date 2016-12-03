#!/usr/bin/python3


def count_stairs(stairs: str):
    up = stairs.count('(')
    down = stairs.count(')')
    return up - down


def should_quit(command):
    return command in ["quit", "q"]


if __name__ == "__main__":
    input_file = ""  # type: str
    while not should_quit(input_file):
        input_file = input("input_file: ")  # type: str
        if not should_quit(input_file):
            with open(input_file) as file:
                stairs = file.readline()
                print("Floor I'm on: {}".format(count_stairs(stairs)))
    print("It's over, you can go outside and play now")
