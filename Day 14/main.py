from collections import deque
OUTPUT_TYPE = int


def knot_cycle(lengths: list[int], elements: deque[int], current_position: int = 0, skip_size: int = 0) -> tuple[deque[int], int, int]:
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


def knot_hash(inp: str) -> int:
    lengths: list[int] = [ord(char) for char in inp]
    current_position: int = 0
    skip_size: int = 0
    lengths.extend([17, 31, 73, 47, 23])

    elements: deque[int] = deque()

    for i in range(256):
        elements.append(i)

    for _ in range(64):
        elements, current_position, skip_size = knot_cycle(
            lengths, elements, current_position, skip_size)

    ret: int = 0
    for _ in range(16):
        ret <<= 8
        net_xor: int = 0
        for _ in range(16):
            net_xor ^= elements.popleft()

        ret += net_xor

    return ret


def main_part_1(inp: str) -> OUTPUT_TYPE:
    ret: int = 0
    for i in range(128):
        ret += bin(knot_hash(f"{inp}-{i}")).count("1")
    return ret


def main_part_2(inp: str) -> OUTPUT_TYPE:
    points: set[int] = set()
    for row in range(128):
        for col, char in enumerate(bin(knot_hash(f"{inp}-{row}"))[2:].zfill(128)):
            if char == "1":
                points.add(row * 129 + col)

    groups: int = 0
    while points:
        seen: set[int] = set()
        to_check: set[int] = {points.pop()}

        while to_check:
            new_seen: set[int] = set()
            for i in to_check:
                for diff in [1, -1, 129, -129]:
                    if i + diff not in seen and i + diff in points:
                        new_seen.add(i + diff)

            seen, to_check = seen.union(to_check), new_seen

        points = points.difference(seen)
        groups += 1

    return groups


def main() -> None:
    test_input: str = "flqrgnkx"
    test_output_part_1_expected: OUTPUT_TYPE = 8108
    test_output_part_2_expected: OUTPUT_TYPE = 1242

    input_file: str = "hxtvlmkl"

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
