from collections import defaultdict
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> defaultdict[int, set[int]]:
    ret: defaultdict[int, set[int]] = defaultdict(lambda: set())
    for row in inp:
        start: int
        end: int
        start, end = tuple(map(int, row.split("/")))

        ret[start].add(end)
        ret[end].add(start)

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    connectors: defaultdict[int, set[int]] = parse_inp(inp)
    paths: list[tuple[int, int, set[tuple[int, int]]]] = [(0, 0, set())]
    best: int = 0
    while paths:
        new_paths: list[tuple[int, int, set[tuple[int, int]]]] = []
        for score, curr, used in paths:
            connections: set[int] = connectors[curr]
            best = max(best, score - curr)

            for connector in connections:
                if (curr, connector) in used:
                    continue

                new_paths.append((
                    score + 2 * connector,
                    connector,
                    used.union({(curr, connector), (connector, curr)})
                ))

        paths = new_paths

    return best


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    connectors: defaultdict[int, set[int]] = parse_inp(inp)
    paths: list[tuple[int, int, int, set[tuple[int, int]]]] = [
        (0, 0, 0, set())]
    best: tuple[int, int] = (0, 0)
    while paths:
        new_paths: list[tuple[int, int, int, set[tuple[int, int]]]] = []
        for score, length, curr, used in paths:
            connections: set[int] = connectors[curr]
            best = max(best, (length, score - curr))

            for connector in connections:
                if (curr, connector) in used:
                    continue

                new_paths.append((
                    score + 2 * connector,
                    length + 1,
                    connector,
                    used.union({(curr, connector), (connector, curr)})
                ))

        paths = new_paths

    return best[1]


def main() -> None:
    test_input: str = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 31
    test_output_part_2_expected: OUTPUT_TYPE = 19

    file_location: str = "python/Advent of Code/2017/Day 24/input.txt"
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
