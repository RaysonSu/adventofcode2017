OUTPUT_TYPE = int


def compute(numbers: str, jump: int) -> int:
    ret: int = 0
    for i in range(len(numbers)):
        if numbers[i] == numbers[(i + jump) % len(numbers)]:
            ret += int(numbers[i])

    return ret


def main_part_1(inp: list[str]) -> int:
    return compute(inp[0].strip(), 1)


def main_part_2(inp: list[str]) -> int:
    return compute(inp[0].strip(), len(inp[0].strip()) // 2)


def main() -> None:
    test_input: str = """12131415"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 0
    test_output_part_2_expected: OUTPUT_TYPE = 4

    file_location: str = "python/Advent of Code/2017/Day 1/input.txt"
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
