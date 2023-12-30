OUTPUT_TYPE = str


def main_part_1(inp: list[str], count: int = 16) -> OUTPUT_TYPE:
    order: list[str] = [chr(0x61 + i) for i in range(count)]
    for instruction in inp[0].strip().split(","):
        ins: str
        param_data: str
        ins, param_data = instruction[0], instruction[1:]

        param: list[str] = param_data.split("/")

        if ins == "s":
            order = order[-int(param[0]):] + order[:-int(param[0])]
        elif ins == "x":
            order[int(param[0])], order[int(param[1])] = \
                order[int(param[1])], order[int(param[0])]
        elif ins == "p":
            i: int = order.index(param[0])
            j: int = order.index(param[1])

            order[i] = param[1]
            order[j] = param[0]

    return "".join(order)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    order: list[str] = [chr(0x61 + i) for i in range(16)]
    seen: list[str] = ["".join(order)]
    while True:
        for instruction in inp[0].strip().split(","):
            ins: str
            param_data: str
            ins, param_data = instruction[0], instruction[1:]

            param: list[str] = param_data.split("/")

            if ins == "s":
                order = order[-int(param[0]):] + order[:-int(param[0])]
            elif ins == "x":
                order[int(param[0])], order[int(param[1])] = \
                    order[int(param[1])], order[int(param[0])]
            elif ins == "p":
                i: int = order.index(param[0])
                j: int = order.index(param[1])

                order[i] = param[1]
                order[j] = param[0]

        if "".join(order) in seen:
            return seen[1000000000 % len(seen)]
        else:
            seen.append("".join(order))


def main() -> None:
    test_input: str = """s1,x3/4,pe/b"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = "baedc"
    test_output_part_2_expected: OUTPUT_TYPE = "ghidjklmnopabcef"

    file_location: str = "python/Advent of Code/2017/Day 16/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 5)
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
