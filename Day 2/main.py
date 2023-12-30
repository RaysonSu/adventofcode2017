from itertools import permutations
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[list[int]]:
    ret: list[list[int]] = []
    for row in inp:
        ret.append(list(map(int, row.replace("\t", " ").split(" "))))

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    rows: list[list[int]] = parse_inp(inp)
    ret: int = 0
    for row in rows:
        ret += max(row) - min(row)

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    rows: list[list[int]] = parse_inp(inp)
    ret: int = 0
    for row in rows:
        for x, y in permutations(row, 2):
            if y % x == 0:
                ret += y // x

    return ret


def main() -> None:
    test_input: str = """5 9 2 8
9 4 7 3
3 8 6 5"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 18
    test_output_part_2_expected: OUTPUT_TYPE = 9

    file_location: str = "python/Advent of Code/2017/Day 2/input.txt"
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
