def compute_weight(stack_data: dict[str, tuple[int, list[str]]], node: str) -> tuple[int, list[int]]:
    weight_curr: int
    sub_nodes: list[str]
    weight_curr, sub_nodes = stack_data[node]

    sub_weights: list[int] = [
        compute_weight(stack_data, sub_node)[0]
        for sub_node in sub_nodes
    ]

    weight: int = weight_curr + sum(sub_weights)

    return weight, sub_weights


def parse_inp(inp: list[str]) -> dict[str, tuple[int, list[str]]]:
    ret: dict[str, tuple[int, list[str]]] = {}
    for row in inp:
        row = row.strip()
        data: list[str] = row.split(" ", 2)
        name: str = data[0]
        weight: int = int(data[1][1:-1])
        stacks: list[str] = []

        if len(data) > 2:
            stacks = data[2][3:].split(", ")

        ret[name] = (weight, stacks)

    return ret


def main_part_1(inp: list[str]) -> str:
    stack_data: dict[str, tuple[int, list[str]]] = parse_inp(inp)
    names: set[str] = set(stack_data.keys())

    stacked: set[str] = set()
    for _, children in stack_data.values():
        stacked = stacked.union(set(children))

    diffrence: set[str] = names.difference(stacked)
    return diffrence.pop()


def main_part_2(inp: list[str]) -> int:
    stack_data: dict[str, tuple[int, list[str]]] = parse_inp(inp)
    names: set[str] = set(stack_data.keys())

    stacked: set[str] = set()
    for _, children in stack_data.values():
        stacked = stacked.union(set(children))

    base: str = names.difference(stacked).pop()
    correct_weight: int = -1
    while True:
        _, weights = compute_weight(stack_data, base)
        unique_weights: set[int] = set(weights)

        if len(unique_weights) == 2:
            wrong: int
            for index, weight in enumerate(weights):
                if weights.count(weight) == 1:
                    wrong = index
                else:
                    correct_weight = weight
            base = stack_data[base][1][wrong]
        else:
            return correct_weight - sum(weights)


def main() -> None:
    test_input: str = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: str = "tknk"
    test_output_part_2_expected: int = 60

    file_location: str = "python/Advent of Code/2017/Day 7/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = [x.replace("\n", "") for x in input_file]

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
