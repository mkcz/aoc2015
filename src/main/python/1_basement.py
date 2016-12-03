#!/usr/bin/python3


def to_the_basement(stairs: str):
    floor = 0
    inx = 0
    for stair in list(stairs):
        inx += 1
        if stair is '(':
            floor += 1
        else:
            floor -= 1
        if floor is -1:
            break
    return inx


def should_quit(command):
    return command in ["quit", "q"]


if __name__ == "__main__":
    input_file = ""  # type: str
    while not should_quit(input_file):
        input_file = input("input_file: ")  # type: str
        if not should_quit(input_file):
            with open(input_file) as file:
                stairs = file.readline()
                print("This chap sent me to the basement : {}".format(to_the_basement(stairs)))
    print("It's over, you can go outside and play now")
