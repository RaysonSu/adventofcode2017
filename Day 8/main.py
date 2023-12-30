from collections import defaultdict
OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    regs: defaultdict[str, int] = defaultdict(lambda: 0)
    for row in inp:
        instuction: str
        condition: str
        instuction, condition = tuple(row.strip().split(" if "))

        name: str
        req: str
        name, req = tuple(condition.split(" ", 1))

        cond: bool = eval(f"regs['{name}'] {req}")

        if cond:
            reg: str
            ins: str
            amt: str
            reg, ins, amt = tuple(instuction.split(" "))

            regs[reg] += int(amt) * {"inc": 1, "dec": -1}[ins]

    return max(regs.values())


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    regs: defaultdict[str, int] = defaultdict(lambda: 0)
    max_val: int = 0
    for row in inp:
        instuction: str
        condition: str
        instuction, condition = tuple(row.strip().split(" if "))

        name: str
        req: str
        name, req = tuple(condition.split(" ", 1))

        cond: bool = eval(f"regs['{name}'] {req}")

        if cond:
            reg: str
            ins: str
            amt: str
            reg, ins, amt = tuple(instuction.split(" "))

            regs[reg] += int(amt) * {"inc": 1, "dec": -1}[ins]
            max_val = max(max_val, regs[reg])

    return max_val


def main() -> None:
    test_input: str = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1
    test_output_part_2_expected: OUTPUT_TYPE = 10

    file_location: str = "python/Advent of Code/2017/Day 8/input.txt"
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
