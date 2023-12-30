OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> tuple[str, int, dict[str, tuple[tuple[int, int, str], tuple[int, int, str]]]]:
    inp = [line.strip() for line in inp]

    start: str = inp[0][-2]
    steps: int = int(inp[1][36:-7])
    ret: dict[str, tuple[tuple[int, int, str], tuple[int, int, str]]] = {}

    for i in range(len(inp) // 10):
        base: int = 10 * i + 3
        key: str = inp[base][-2]
        zero_write: int = int(inp[base + 2][-2])
        zero_action: int = 2 * int(inp[base + 3][-3] == "h") - 1
        zero_state: str = inp[base + 4][-2]
        one_write: int = int(inp[base + 6][-2])
        one_action: int = 2 * int(inp[base + 7][-3] == "h") - 1
        one_state: str = inp[base + 8][-2]

        zero: tuple[int, int, str] = (zero_write, zero_action, zero_state)
        one: tuple[int, int, str] = (one_write, one_action, one_state)

        ret[key] = (zero, one)

    return start, steps, ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    state: str
    steps: int
    instructions: dict[str, tuple[tuple[int, int, str], tuple[int, int, str]]]
    state, steps, instructions = parse_inp(inp)

    pointer: int = 0
    tape: list[int] = [0]
    for _ in range(steps):
        current_value: int = tape[pointer]

        write: int
        action: int
        write, action, state = instructions[state][current_value]

        tape[pointer] = write
        pointer += action

        if pointer < 0:
            tape.insert(0, 0)
            pointer += 1
        elif pointer >= len(tape):
            tape.append(0)
    return sum(tape)


def main() -> None:
    test_input: str = """Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 3

    file_location: str = "python/Advent of Code/2017/Day 25/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()


if __name__ == "__main__":
    main()
