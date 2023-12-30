from collections import defaultdict
OUTPUT_TYPE = int


def next_point(current_point: tuple[int, int]) -> tuple[int, int]:
    x: int
    y: int

    x, y = current_point

    if x == -y and x >= 0:
        return x + 1, y

    if x > y and y > -x:
        return x, y + 1

    if y >= x and y > -x:
        return x - 1, y

    if y > x and -y >= x:
        return x, y - 1

    if x >= y and -y > x:
        return x + 1, y

    raise ValueError("oh crap!")


def main_part_1(inp: int) -> OUTPUT_TYPE:
    point: tuple[int, int] = (0, 0)
    for _ in range(inp - 1):
        point = next_point(point)

    return abs(point[0]) + abs(point[1])


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    grid: defaultdict[tuple[int, int], int] = defaultdict(lambda: 0)
    point: tuple[int, int] = (0, 0)
    grid[point] = 1

    while True:
        point = next_point(point)
        total: int = 0
        for diff_x in range(-1, 2):
            for diff_y in range(-1, 2):
                total += grid[(point[0] + diff_x, point[1] + diff_y)]

        grid[point] = total

        if total > inp:
            return total


def main() -> None:
    test_input: int = 1024
    test_output_part_1_expected: OUTPUT_TYPE = 31
    test_output_part_2_expected: OUTPUT_TYPE = 1968

    input_file: int = 368078

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input)

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
