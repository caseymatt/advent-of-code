def create_input() -> [int]:
    instructions = []
    with open('/Users/mattcm/Desktop/advent-of-code-2021/advent-of-code-2-input.txt') as input:
        for line in input:
            instruction = line.strip('\n')
            instructions.append(tuple(instruction.split(" ")))
    return instructions

def calc_distance(input: [str, int]) -> int:
    # Horizontal position * Depth
    x_position = y_position = 0
    for instruction, amount in input:
        amount = int(amount)
        if instruction == "forward":
            x_position += amount
        if instruction == "up":
            y_position -= amount
        if instruction == "down":
            y_position += amount

    return x_position * y_position

def calc_distance_using_aim(input: [int]) -> int:
    x_position = y_position = aim = 0
    for instruction, amount in input:
        amount = int(amount)
        if instruction == "forward":
            x_position += amount
            y_position += aim * amount
        if instruction == "up":
            aim -= amount
        if instruction == "down":
            aim += amount

    return x_position * y_position

def main():
    input = create_input()
    testCase = [('forward', '5'), ('down', '5'), ('forward', '8'), ('up', '3'), ('down', '8'), ('forward', '2')]
    print(f"{calc_distance(input) = }")
    print(f"{calc_distance_using_aim(input) = }")

if __name__ == '__main__':
    main()
