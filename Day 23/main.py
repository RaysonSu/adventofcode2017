from collections import defaultdict

OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    regs: defaultdict[str, int] = defaultdict(lambda: 0)
    instruction: int = 0
    count: int = 0
    while True:
        jumped: bool = False
        if instruction >= len(inp):
            return count

        line: str = inp[instruction].strip()
#        print(instruction, line, regs.items())

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

        if opcode == "set":
            regs[acting] = amount
        elif opcode == "sub":
            regs[acting] -= amount
        elif opcode == "mul":
            regs[acting] *= amount
            count += 1
        elif opcode == "jnz":
            if regs[acting] or (acting.isnumeric() and acting != "0"):
                instruction += amount
                jumped = True

        if not jumped:
            instruction += 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    regs: defaultdict[str, int] = defaultdict(lambda: 0)
    regs["a"] = 1
    instruction: int = 0
    count: int = 0
    for _ in range(100):
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

        if opcode == "set":
            regs[acting] = amount
        elif opcode == "sub":
            regs[acting] -= amount
        elif opcode == "mul":
            regs[acting] *= amount
            count += 1
        elif opcode == "jnz":
            if regs[acting] or (acting.isnumeric() and acting != "0"):
                instruction += amount
                jumped = True

        if not jumped:
            instruction += 1

    return compute(regs["b"], regs["c"])


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n % 2 == 0 and n > 2:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def compute(low: int, high: int) -> int:
    ret: int = 0

    for n in range(low, high + 1, 17):
        if not is_prime(n):
            ret += 1

    return ret


def main() -> None:
    file_location: str = "python/Advent of Code/2017/Day 23/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    print(f"Part 1: {main_part_1(input_file)}")
    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
