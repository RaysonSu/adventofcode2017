OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> dict[str, str]:
    ret: dict[str, str] = {}
    for row in inp:
        initial: str
        end: str

        initial, end = tuple(row.strip().split(" => "))
        initial = compress(normalize(uncompress(initial)))
        ret[initial] = end

    return ret


def transpose(grid: list[str]) -> list[str]:
    return ["".join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]


def transpose_2d_list(grid: list[list[str]]) -> list[list[str]]:
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


def rotate90(grid: list[str]) -> list[str]:
    return transpose(grid)[::-1]


def reflect_vertical(grid: list[str]) -> list[str]:
    return transpose(transpose(grid)[::-1])


def generate_rotations(grid: list[str]) -> list[list[str]]:
    ret: list[list[str]] = []
    for reflect in [False, True]:
        for rotations in range(4):
            tmp_image = grid.copy()
            for _ in range(rotations):
                tmp_image = rotate90(tmp_image)

            if reflect:
                tmp_image = reflect_vertical(tmp_image)
            ret.append(tmp_image)
    return ret


def calc_value(tile: list[str]) -> int:
    return int(("".join(tile) + "#").replace("#", "1").replace(".", "0"), 2) << len(tile) ** 3


def iterate(grid: list[str], rules: dict[str, str]) -> list[str]:
    length: int = 2 if len(grid) % 2 == 0 else 3
    ret: list[str] = []
    for row_split in range(len(grid) // length):
        buffer: list[str] = ["" for _ in range(length + 1)]
        for col_split in range(len(grid) // length):
            tile: list[str] = [
                grid[i][col_split * length:(col_split + 1) * length]
                for i in range(row_split * length, (row_split + 1) * length)
            ]

            compressed: str = compress(normalize(tile))
            new_tile: str = rules[compressed]
            uncompressed: list[str] = uncompress(new_tile)

            for i, row in enumerate(uncompressed):
                buffer[i] += row

        ret.extend(buffer)

    return ret


def uncompress(compressed: str) -> list[str]:
    return compressed.split("/")


def compress(uncompressed: list[str]) -> str:
    return "/".join(uncompressed)


def normalize(grid: list[str]) -> list[str]:
    best: int = 0
    ret: list[str]

    for rotation in generate_rotations(grid):
        value = calc_value(rotation)
        if value > best:
            best = value
            ret = rotation

    return ret


def main_part_1(inp: list[str], iterations: int = 5) -> OUTPUT_TYPE:
    initial: str = ".#./..#/###"
    grid: list[str] = uncompress(initial)
    rules: dict[str, str] = parse_inp(inp)

    for _ in range(iterations):
        grid = iterate(grid, rules)

    return compress(grid).count("#")


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return main_part_1(inp, 18)


def main() -> None:
    test_input: str = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 12

    file_location: str = "python/Advent of Code/2017/Day 21/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 2)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
