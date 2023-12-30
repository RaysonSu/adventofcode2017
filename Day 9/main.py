from typing import Any

OUTPUT_TYPE = int


def parse_garbage(garbage: str) -> Any:
    if garbage == "":
        return None

    if garbage[0] != "{":
        return garbage[1:-1]

    index: int = 1
    depth: int = 0
    in_garbage: bool = False
    current: str = ""
    ret: list[Any] = []
    while index < len(garbage) - 1:
        char: str = garbage[index]
        if char == "!":
            index += 2
            continue

        if char == "{" and not in_garbage:
            depth += 1
        elif char == "}" and not in_garbage:
            depth -= 1
        elif char == "<" and not in_garbage:
            in_garbage = True
        elif char == ">":
            in_garbage = False

        if in_garbage or depth != 0 or char != ",":
            current += char
        else:
            ret.append(parse_garbage(current))
            current = ""

        index += 1

    ret.append(parse_garbage(current))
    return ret


def count_score(inp: Any, base: int = 1) -> int:
    ret: int = 0
    ret += base
    for i in inp:
        if isinstance(i, list):
            ret += count_score(i, base + 1)

    return ret


def count_garbage(inp: Any) -> int:
    ret: int = 0
    for i in inp:
        if isinstance(i, list):
            ret += count_garbage(i)
        elif isinstance(i, str):
            ret += len(i)

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    return count_score(parse_garbage(inp[0].strip()))


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return count_garbage(parse_garbage(inp[0].strip()))


def main() -> None:
    test_input: str = """{{{},{},{{}}}}"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 16
    test_output_part_2_expected: OUTPUT_TYPE = 0

    file_location: str = "python/Advent of Code/2017/Day 9/input.txt"
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
