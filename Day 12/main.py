OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[list[int]]:
    ret: list[list[int]] = []
    for line in inp:
        ret.append(eval(f"[{line.split('> ')[1]}]"))

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    paths: list[list[int]] = parse_inp(inp)

    seen: set[int] = set()
    to_check: set[int] = {0}

    while to_check:
        new_seen: set[int] = set()
        for i in to_check:
            for j in paths[i]:
                if j not in seen:
                    new_seen.add(j)

        seen, to_check = seen.union(to_check), new_seen

    return len(seen)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    paths: list[list[int]] = parse_inp(inp)
    programs_remaining: set[int] = set(range(len(paths)))

    groups: int = 0
    while programs_remaining:
        seen: set[int] = set()
        to_check: set[int] = {programs_remaining.pop()}

        while to_check:
            new_seen: set[int] = set()
            for i in to_check:
                for j in paths[i]:
                    if j not in seen:
                        new_seen.add(j)

            seen, to_check = seen.union(to_check), new_seen

        programs_remaining = programs_remaining.difference(seen)
        groups += 1

    return groups


def main() -> None:
    test_input: str = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 6
    test_output_part_2_expected: OUTPUT_TYPE = 2

    file_location: str = "python/Advent of Code/2017/Day 12/input.txt"
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
