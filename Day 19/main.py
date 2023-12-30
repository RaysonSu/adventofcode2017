def energised(inp: list[str], initial: tuple[int, int, int]) -> tuple[str, int]:
    beam: tuple[int, int, int] = initial
    path: str = ""
    count: int = 0
    while True:
        count += 1
        new_loc: tuple[int, int] = (
            beam[0] + [1, 0, -1, 0][beam[2]],
            beam[1] + [0, -1, 0, 1][beam[2]]
        )

        if new_loc[0] < 0 or new_loc[0] >= len(inp[0]) or new_loc[1] < 0 or new_loc[1] >= len(inp):
            return path, count

        tile: str = inp[new_loc[1]][new_loc[0]]

        new_direction: int
        if tile in "|-":
            new_direction = beam[2]
        elif tile.isalpha():
            path += tile
            new_direction = beam[2]
        elif tile == " ":
            return path, count
        elif tile == "+":
            for diff in [1, 3]:
                new_new_loc: tuple[int, int] = (
                    new_loc[0] + [1, 0, -1, 0][(beam[2] + diff) % 4],
                    new_loc[1] + [0, -1, 0, 1][(beam[2] + diff) % 4]
                )

                if new_new_loc[0] < 0 \
                        or new_new_loc[0] >= len(inp[0]) \
                        or new_new_loc[1] < 0 \
                        or new_new_loc[1] >= len(inp):
                    continue

                if inp[new_new_loc[1]][new_new_loc[0]] == " ":
                    continue

                new_direction = (beam[2] + diff) % 4
                break

        beam = new_loc + (new_direction,)


def main_part_1(inp: list[str]) -> str:
    return energised(inp, (inp[0].index("|"), 0, 3))[0]


def main_part_2(inp: list[str]) -> int:
    ret: int = 0
    return energised(inp, (inp[0].index("|"), 0, 3))[1]


def main() -> None:
    test_input: str = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: str = "ABCDEF"
    test_output_part_2_expected: int = 38

    file_location: str = "python/Advent of Code/2017/Day 19/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: str = main_part_1(test_input_parsed)
    test_output_part_2: int = main_part_2(test_input_parsed)

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
