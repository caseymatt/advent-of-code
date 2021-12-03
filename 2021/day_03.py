import copy

def create_input() -> [int]:
    diagnostics = []
    with open('/Users/mattcm/Desktop/advent-of-code-2021/advent-of-code-3-input.txt') as input:
        for line in input:
            diagnostic = line.strip('\n')
            diagnostics.append(diagnostic)
    return diagnostics

def convert_to_matrix(input: [str]) -> [[int]]:
    output = []
    for diagnostic in input:
        char_array = []
        for character in diagnostic:
            char_array.append(int(character))
        output.append(char_array)
    return output

def find_bit_criteria(input: [[int]], type: str = None) -> [int]:
    criteria = []
    count_zeros = count_ones = 0
    for c in range(len(input[0])):
        for r in range(len(input)):
            # print(f"{r = }", f"{c = }", f"{input[r][c] = }")
            if input[r][c] == 0:
                count_zeros += 1
            else:
                count_ones += 1
        criteria.append("0") if count_zeros > count_ones else criteria.append("1")
        count_zeros = count_ones = 0
        bit_criteria = criteria

    if type == "INVERTED":
        bit_criteria = []
        for bit in criteria:
            bit_criteria.append(str(int(not int(bit))))

    return bit_criteria

def decode_power_consumption_rates(input: [[int]], type: str) -> int:
    if type == "gamma":
        gamma_rate = find_bit_criteria(input)
        return int("".join(gamma_rate), 2)
    if type == "epsilon":
        epsilon_rate = find_bit_criteria(input, "INVERTED")
        return int("".join(epsilon_rate), 2)
    return -1

def find_life_support_ratings(input: [[int]], type: str) -> int:
    output = copy.deepcopy(input)
    c = 0
    while len(output) > 1 and c < len(output[0]):
        if type == "oxygen":
            bit = find_bit_criteria(output)[c]
        if type == "co2":
            bit = find_bit_criteria(output, "INVERTED")[c]
        output[:] = filter(lambda arr: arr[c] == int(bit), output)
        c += 1
    return int("".join(map(str, output[0])), 2)

def main():
    # test_case = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    input = create_input()
    input = convert_to_matrix(input)

    gamma_rate = decode_power_consumption_rates(input, "gamma")
    epsilon_rate = decode_power_consumption_rates(input, "epsilon")
    print("(gamma_rate * epsilon_rate) {} * {} = {}".format(gamma_rate, epsilon_rate, gamma_rate * epsilon_rate))

    oxygen_rating = find_life_support_ratings(input, "oxygen")
    co2_rating = find_life_support_ratings(input, "co2")
    print("(oxygen_rating * co2_rating) {} * {} = {}".format(oxygen_rating, co2_rating, oxygen_rating * co2_rating))

if __name__ == '__main__':
    main()
