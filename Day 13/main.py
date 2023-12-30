OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for row in inp:
        x, y = tuple(map(int, row.split(": ")))
        if x % (2 * y - 2) == 0:
            ret += x * y
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    while True:
        for row in inp:
            x, y = tuple(map(int, row.split(": ")))
            if (x + ret) % (2 * y - 2) == 0:
                break
        else:
            return ret

        ret += 1


def main() -> None:
    test_input: str = """0: 3
1: 2
4: 4
6: 4"""
    test_input_parsed: list[str] = test_input.splitlines(True)
    test_output_part_1_expected: OUTPUT_TYPE = 24
    test_output_part_2_expected: OUTPUT_TYPE = 10

    file_location: str = "python/Advent of Code/2017/Day 13/input.txt"
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
