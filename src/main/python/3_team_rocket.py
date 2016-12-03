#!/usr/bin/python3


class Counter:
    def __init__(self, start_value=0):
        self.count = start_value

    def increment(self):
        self.count += 1


class PresentCounter:
    directions = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}  # type: dict[str, (int, int)]
    present_distribution = {(0, 0): Counter(1)}  # type: dict[(int, int), Counter]
    coords = {'santa': [0, 0], 'robo-santa': [0, 0]}  # type: dict[str, [int, int]]

    def reset(self):
        self.present_distribution.clear()
        self.present_distribution[(0, 0)] = Counter(1)
        self.coords['santa'] = [0, 0]
        self.coords['robo-santa'] = [0, 0]

    def navigate(self, _directions: str):
        current = 'santa'
        for direction in list(_directions):
            self.coords[current][0] += self.directions[direction][0]
            self.coords[current][1] += self.directions[direction][1]
            self.present_distribution.setdefault((self.coords[current][0], self.coords[current][1]), Counter()) \
                .increment()
            current = 'santa' if current == 'robo-santa' else 'robo-santa'

    def houses_visited(self):
        return len(self.present_distribution)


def should_quit(_command):
    return _command in ["quit", "q"]


if __name__ == "__main__":
    input_file = ""  # type: str
    present_counter = PresentCounter()
    while not should_quit(input_file):
        input_file = input("input_file: ")  # type: str
        if not should_quit(input_file):
            present_counter.reset()
            with open(input_file) as file:
                directions = file.readline()
                present_counter.navigate(directions)
                print("Santa and Robo-Santa have visited {} houses".format(present_counter.houses_visited()))
    print("It's over, you can go outside and play now")
