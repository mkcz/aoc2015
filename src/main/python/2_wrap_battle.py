#!/usr/bin/python3


class WrappingPaperCounter:
    total_size = 0  # type: int

    def reset(self):
        self.total_size = 0

    def consume(self, present_dimensions: str):
        (l, w, h) = [int(dim) for dim in present_dimensions.split('x')]
        lw = l * w  # type: int
        lh = l * h  # type: int
        wh = w * h  # type: int
        self.total_size += 2 * lw + 2 * lh + 2 * wh + min(lw, lh, wh)


def should_quit(command):
    return command in ["quit", "q"]


if __name__ == "__main__":
    input_file = ""  # type: str
    wrapping_paper_counter = WrappingPaperCounter()
    while not should_quit(input_file):
        input_file = input("input_file: ")  # type: str
        if not should_quit(input_file):
            wrapping_paper_counter.reset()
            with open(input_file) as file:
                present_sizes = file.readlines()
                for present_size in present_sizes:
                    wrapping_paper_counter.consume(present_size)
                print("We need {} square feet of wrapping paper".format(wrapping_paper_counter.total_size))
    print("It's over, you can go outside and play now")
