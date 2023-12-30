OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    a: int = int(inp[0][24:])
    b: int = int(inp[1][24:])

    ret: int = 0
    for _ in range(40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647

        if (a & 0xffff) == (b & 0xffff):
            ret += 1

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    a: int = int(inp[0][24:])
    b: int = int(inp[1][24:])

    ret: int = 0
    for _ in range(5000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647

        while a % 4:
            a = (a * 16807) % 2147483647
        while b % 8:
            b = (b * 48271) % 2147483647

        if (a & 0xffff) == (b & 0xffff):
            ret += 1

    return ret


def main() -> None:
    file_location: str = "python/Advent of Code/2017/Day 15/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    print(f"Part 1: {main_part_1(input_file)}")
    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
