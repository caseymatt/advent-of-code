def create_input() -> [int]:
    depths = []
    with open('/Users/mattcm/Desktop/advent-of-code-2021/advent-of-code-1-input.txt') as input:
        for line in input:
            depth = line.strip('\n')
            depths.append(int(depth))
    return depths

def count_single_increases(input: [int]) -> int:
    count = 0
    n = len(input)
    for i in range(1, n):
        if input[i] > input[i - 1]:
            count += 1
    return count

def count_group_increases(input: [int]) -> int:
    count = 0
    n = len(input)
    for i in range(1, n-2):
        prev_sum = input[i-1] + input[i] + input[i+1]
        curr_sum = input[i] + input[i+1] + input[i+2]
        if curr_sum > prev_sum:
            count += 1
    return count

def main():
    input = create_input()
    print(f"{count_single_increases(input) = }")
    print(f"{count_group_increases(input) = }")

if __name__ == '__main__':
    main()
