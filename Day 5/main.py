from __future__ import annotations

OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    instructions: list[int] = list(map(int, inp))

    index: int = 0
    jumps: int = 0

    while index >= 0 and index < len(instructions):
        prev_index: int = index
        index += instructions[index]

        instructions[prev_index] += 1

        jumps += 1

    return jumps


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    instructions: list[int] = list(map(int, inp))

    index: int = 0
    jumps: int = 0

    while index >= 0 and index < len(instructions):
        prev_index: int = index
        index += instructions[index]

        if instructions[prev_index] >= 3:
            instructions[prev_index] -= 1
        else:
            instructions[prev_index] += 1

        jumps += 1

    return jumps


def main() -> None:
    test_input: str = """0
3
0
1
-3"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 5
    test_output_part_2_expected: OUTPUT_TYPE = 10

    file_location: str = "python/Advent of Code/2017/Day 5/input.txt"
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
