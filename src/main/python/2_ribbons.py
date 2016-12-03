#!/usr/bin/python3


class RibbonCounter:
    total_length = 0  # type: int

    def reset(self):
        self.total_length = 0

    def consume(self, present_dimensions: str):
        (l, w, h) = [int(dim) for dim in present_dimensions.split('x')]
        (a, b) = self._min_two([l, w, h])
        self.total_length += 2 * a + 2 * b + l * w * h

    @staticmethod
    def _min_two(dimensions: list):
        min_dim = min(dimensions)
        dimensions.remove(min_dim)
        if len(dimensions) <= 1:
            return min_dim, min_dim
        return min_dim, min(dimensions)


def should_quit(command):
    return command in ["quit", "q"]


if __name__ == "__main__":
    input_file = ""  # type: str
    ribbon_counter = RibbonCounter()
    while not should_quit(input_file):
        input_file = input("input_file: ")  # type: str
        if not should_quit(input_file):
            ribbon_counter.reset()
            with open(input_file) as file:
                present_sizes = file.readlines()
                for present_size in present_sizes:
                    ribbon_counter.consume(present_size)
                print("We need {} feet of ribbon".format(ribbon_counter.total_length))
    print("It's over, you can go outside and play now")
