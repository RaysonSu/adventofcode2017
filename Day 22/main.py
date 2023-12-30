from collections import defaultdict
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> tuple[defaultdict[tuple[int, int], int], tuple[int, int]]:
    ret: defaultdict[tuple[int, int], int] = defaultdict(lambda: 0)

    for row_index, row in enumerate(inp):
        for col_index, char in enumerate(row):
            if char == "#":
                ret[(col_index, row_index)] = 2

    return ret, (len(inp[0].strip()) // 2, len(inp) // 2)


def print_grid(infected: defaultdict[tuple[int, int], int], current_state: tuple[int, int]) -> None:
    min_x: int = min([x for x, _ in infected.keys()])
    min_y: int = min([y for _, y in infected.keys()])
    max_x: int = max([x for x, _ in infected.keys()])
    max_y: int = max([y for _, y in infected.keys()])

    min_x = min(min_x, current_state[0])
    min_y = min(min_y, current_state[1])
    max_x = max(max_x, current_state[0])
    max_y = max(max_y, current_state[1])

    for y in range(min_y, max_y + 1):
        to_print: str = ""
        for x in range(min_x, max_x + 1):
            if (x, y) == current_state:
                to_print += "["
            else:
                to_print += " "

            to_print += ".W#F"[infected[(x, y)]]

            if (x, y) == current_state:
                to_print += "]"
            else:
                to_print += " "
        print(to_print)


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    current_state: tuple[int, int]
    states: defaultdict[tuple[int, int], int]
    states, current_state = parse_inp(inp)

    direction: int = 1
    count: int = 0
    for _ in range(10000):
        direction += 1 - states[current_state]

        if states[current_state] == 0:
            count += 1

        states[current_state] += 2
        states[current_state] %= 4
        direction %= 4

        current_state = (
            current_state[0] + [1, 0, -1, 0][direction],
            current_state[1] + [0, -1, 0, 1][direction]
        )

    return count


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    current_state: tuple[int, int]
    states: defaultdict[tuple[int, int], int]
    states, current_state = parse_inp(inp)

    direction: int = 1
    count: int = 0
    for _ in range(10000000):
        direction += 1 - states[current_state]

        if states[current_state] == 1:
            count += 1

        states[current_state] += 1
        states[current_state] %= 4
        direction %= 4

        current_state = (
            current_state[0] + [1, 0, -1, 0][direction],
            current_state[1] + [0, -1, 0, 1][direction]
        )

    return count


def main() -> None:
    test_input: str = """..#
#..
..."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 5587
    test_output_part_2_expected: OUTPUT_TYPE = 2511944

    file_location: str = "python/Advent of Code/2017/Day 22/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
