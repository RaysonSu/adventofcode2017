from collections import deque


def knot_hash(lengths: list[int], elements: deque[int], current_position: int = 0, skip_size: int = 0) -> tuple[deque[int], int, int]:
    elements.rotate(-current_position)

    for length in lengths:
        selected: list[int] = []
        for _ in range(length):
            selected.append(elements.popleft())

        for i in selected:
            elements.appendleft(i)

        elements.rotate(-length - skip_size)
        current_position += length + skip_size
        skip_size += 1

    elements.rotate(current_position)

    return elements, current_position % len(elements), skip_size


def main_part_1(inp: list[str], element_count: int = 256) -> int:
    lengths: list[int] = eval(f"[{inp[0].strip()}]")
    elements: deque[int] = deque()

    for i in range(element_count):
        elements.append(i)

    elements, _, _ = knot_hash(lengths, elements)

    return elements.popleft() * elements.popleft()


def main_part_2(inp: list[str]) -> str:
    lengths: list[int] = [ord(char) for char in inp[0].strip()]
    current_position: int = 0
    skip_size: int = 0
    lengths.extend([17, 31, 73, 47, 23])

    elements: deque[int] = deque()

    for i in range(256):
        elements.append(i)

    for _ in range(64):
        elements, current_position, skip_size = knot_hash(
            lengths, elements, current_position, skip_size)

    ret: str = ""
    for _ in range(16):
        net_xor: int = 0
        for _ in range(16):
            net_xor ^= elements.popleft()

        ret += hex(net_xor)[2:].zfill(2)

    return ret


def main() -> None:
    test_input: str = """1,2,3"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: int = 0
    test_output_part_2_expected: str = "3efbe78a8d82f29979031a4aa0b16a9d"

    file_location: str = "python/Advent of Code/2017/Day 10/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: int = main_part_1(test_input_parsed, 5)
    test_output_part_2: str = main_part_2(test_input_parsed)

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
