from collections import deque


OUTPUT_TYPE = int


def main_part_1(inp: int) -> OUTPUT_TYPE:
    data: deque[int] = deque()
    data.append(0)

    for i in range(1, 2018):
        data.rotate(-inp)
        data.append(i)
    data.rotate(-1)
    return data.pop()


def main_part_2(inp: int) -> OUTPUT_TYPE:
    data: deque[int] = deque()
    data.append(0)

    for i in range(1, 50000000):
        data.rotate(-inp)
        data.append(i)
    data.rotate(-data.index(0))
    data.popleft()
    return data.popleft()


def main() -> None:
    test_input: int = 3
    test_output_part_1_expected: OUTPUT_TYPE = 638
    test_output_part_2_expected: OUTPUT_TYPE = 1222153

    input_file: int = 366

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
