from collections import defaultdict
OUTPUT_TYPE = int


class Program:
    def __init__(self,
                 regs: defaultdict[str, int],
                 inps: list[int],
                 ins: int,
                 count: int) -> None:
        self.regs: defaultdict[str, int] = regs
        self.inps: list[int] = inps
        self.ins: int = ins
        self.count: int = count

    def __str__(self) -> str:
        return f"{self.regs.values()} {self.inps}"


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    regs: defaultdict[str, int] = defaultdict(lambda: 0)
    instruction: int = 0
    last_freq: int = -1
    while True:
        jumped: bool = False
        line: str = inp[instruction].strip()

        opcode: str
        params: list[str] = []
        opcode, params = line.split(" ")[0], line.split(" ")[1:]

        acting: str = params[0]
        amount: int
        if len(params) == 2:
            try:
                amount = int(params[1])
            except ValueError as _:
                amount = regs[params[1]]

        if opcode == "snd":
            last_freq = regs[acting]
        elif opcode == "set":
            regs[acting] = amount
        elif opcode == "add":
            regs[acting] += amount
        elif opcode == "mul":
            regs[acting] *= amount
        elif opcode == "mod":
            regs[acting] %= amount
        elif opcode == "rcv":
            if regs[acting]:
                return last_freq
        elif opcode == "jgz":
            if regs[acting] > 0:
                instruction += amount
                jumped = True

        if not jumped:
            instruction += 1


def run_program(p_a: Program, p_b: Program, instructions: list[str]) -> bool:
    jumped: bool = False
    line: str = instructions[p_a.ins].strip()

    opcode: str
    params: list[str] = []
    opcode, params = line.split(" ")[0], line.split(" ")[1:]

    acting: str = params[0]
    amount: int
    if len(params) == 2:
        try:
            amount = int(params[1])
        except ValueError as _:
            amount = p_a.regs[params[1]]

    if opcode == "snd":
        try:
            p_b.inps.append(int(acting))
        except ValueError as _:
            p_b.inps.append(p_a.regs[acting])
        p_a.count += 1
    elif opcode == "set":
        p_a.regs[acting] = amount
    elif opcode == "add":
        p_a.regs[acting] += amount
    elif opcode == "mul":
        p_a.regs[acting] *= amount
    elif opcode == "mod":
        p_a.regs[acting] %= amount
    elif opcode == "rcv":
        if p_a.inps:
            p_a.regs[acting] = p_a.inps.pop(0)
        else:
            return False
    elif opcode == "jgz":
        checked: int
        try:
            checked = int(acting)
        except ValueError as _:
            checked = p_a.regs[acting]
        if checked > 0:
            p_a.ins += amount
            jumped = True

    if not jumped:
        p_a.ins += 1
    return True


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    p_a: Program = Program(defaultdict(lambda: 0), [], 0, 0)
    p_b: Program = Program(defaultdict(lambda: 0), [], 0, 0)

    p_a.regs["p"] = 0
    p_b.regs["p"] = 1

    while True:
        p_al: bool = run_program(p_a, p_b, inp)
        p_bl: bool = run_program(p_b, p_a, inp)

#        print(p_a)
#        print(p_b)
#        print()

        if not (p_al or p_bl):
            return p_b.count


def main() -> None:
    test_input: str = """set a 1
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 0
    test_output_part_2_expected: OUTPUT_TYPE = 3

    file_location: str = "python/Advent of Code/2017/Day 18/input.txt"
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
