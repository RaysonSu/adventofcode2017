OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[int]:
    return list(map(int, inp[0].replace("\t", " ").split(" ")))


def redistribute(data: list[int]) -> list[int]:
    data = data.copy()
    start: int = data.index(max(data))
    amount_left: int = max(data)
    data[start] = 0

    while amount_left:
        start += 1
        start %= len(data)
        data[start] += 1
        amount_left -= 1

    return data


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    stacks: list[int] = parse_inp(inp)
    seen: set[tuple[int, ...]] = set()
    count: int = 0

    while True:
        if tuple(stacks) in seen:
            return count

        seen.add(tuple(stacks))
        stacks = redistribute(stacks)
        count += 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    stacks: list[int] = parse_inp(inp)
    seen: list[tuple[int, ...]] = []
    count: int = 0

    while True:
        if tuple(stacks) in seen:
            return count - seen.index(tuple(stacks))

        seen.append(tuple(stacks))
        stacks = redistribute(stacks)
        count += 1


def main() -> None:
    test_input: str = """0 2 7 0"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 5
    test_output_part_2_expected: OUTPUT_TYPE = 4

    file_location: str = "python/Advent of Code/2017/Day 6/input.txt"
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
