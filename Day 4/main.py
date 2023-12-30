OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[list[str]]:
    return [list(row.strip().split(" ")) for row in inp]


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    phrases: list[list[str]] = parse_inp(inp)

    ret: int = 0
    for row in phrases:
        if len(row) == len(set(row)):
            ret += 1

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    phrases: list[list[str]] = parse_inp(inp)

    ret: int = 0
    for row in phrases:
        for i in range(len(row)):
            row[i] = "".join(sorted(row[i]))

        if len(row) == len(set(row)):
            ret += 1

    return ret


def main() -> None:
    test_input: str = """aa bb cc dd ee
aa bb cc dd aa
abcde xyz ecdab
iiii oiii ooii oooi oooo"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 3
    test_output_part_2_expected: OUTPUT_TYPE = 2

    file_location: str = "python/Advent of Code/2017/Day 4/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = list(map(str.strip, input_file))

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
