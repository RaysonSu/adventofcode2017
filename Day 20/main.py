from numpy import array as Vector
from numpy import int_ as npint
from numpy.typing import NDArray
from collections import defaultdict


vector_int = NDArray[npint]
OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    best: int = 10000000000
    best_index: int = -1
    for index, line in enumerate(inp):
        a: str = line.split(", ")[2]
        amount: int = sum(map(abs, eval(f"[{a.strip()[3:-1]}]")))
        if amount < best:
            best_index = index
            best = amount
    return best_index


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    data: list[list[vector_int]] = []
    for line in inp:
        splited: list[str] = line.strip().split(", ")
        data.append([Vector(eval(f"[{a[3:-1]}]")) for a in splited])

    coeff: list[tuple[vector_int, vector_int, vector_int]] = [
        (
            2 * params[0],
            2 * params[1] + params[2],
            params[2]
        )
        for params in data
    ]

    for t in range(100):
        positions: list[tuple[int, int, int]] = []
        counts: defaultdict[tuple[int, int, int], int] = defaultdict(lambda: 0)
        for c, b, a in coeff:
            pos: tuple[int, int, int] = tuple(a * t ** 2 + b * t + c)
            positions.append(pos)
            counts[pos] += 1

        new_coeff: list[tuple[vector_int, vector_int, vector_int]] = []
        for index, position in enumerate(positions):
            if counts[position] == 1:
                new_coeff.append(coeff[index])

        coeff = new_coeff
#        print(t)

    return len(new_coeff)


def main() -> None:
    test_input: str = """p=<0,0,1>, v=< 0,0,0>, a=< 0,0,0> 
p=<-6,0,0>, v=< 3,0,0>, a=< 1,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 1,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 1,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 1,0,0>"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 0
    test_output_part_2_expected: OUTPUT_TYPE = 2

    file_location: str = "python/Advent of Code/2017/Day 20/input.txt"
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
