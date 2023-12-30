OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    line: str = inp[0].strip() + ","

    count = {char: line.count(char + ",")
             for char in ["n", "ne", "nw", "s", "se", "sw"]}

    x = count["n"] - count["s"]
    y = count["sw"] - count["ne"]
    z = count["nw"] - count["se"]

    return max(abs(x), abs(y)) + abs(z)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    line: str = inp[0].strip()

    x = 0
    y = 0
    z = 0
    m = 0
    for i in line.split(","):
        if i == "n":
            x += 1
        elif i == "s":
            x -= 1
        elif i == "sw":
            y += 1
        elif i == "ne":
            y -= 1
        elif i == "nw":
            z += 1
        elif i == "se":
            z -= 1

        m = max(m, max(abs(x), abs(y)) + abs(z))

    return m


def main() -> None:
    test_input: str = """se,sw,se,sw,sw"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 5
    test_output_part_2_expected: OUTPUT_TYPE = 5

    file_location: str = "python/Advent of Code/2017/Day 11/input.txt"
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
