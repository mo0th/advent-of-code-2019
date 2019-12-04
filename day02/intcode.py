def run_intcode(intcode):
    i = 0
    while i < len(intcode) and intcode[i] != 99:
        opcode = intcode[i]
        num1 = intcode[intcode[i + 1]]
        num2 = intcode[intcode[i + 2]]
        dest_index = intcode[i + 3]
        # print("dest_index", dest_index)
        if dest_index < len(intcode):
            if opcode == 1:
                intcode[dest_index] = num1 + num2
            elif opcode == 2:
                intcode[dest_index] = num1 * num2
        else:
            i += 4
            continue

        i += 4

    return intcode


def get_codes():
    with open('input.txt', 'r') as f:
        input_line = f.readline().strip()
        return [int(i) for i in input_line.split(',')]


codes = get_codes()
desired_output = 19690720

# set up for '1202 program alarm'
# codes[1] = 12
# codes[2] = 2

codes[1] = noun = 64  # noun adds 300000
codes[2] = verb = 21  # verb adds 1
result = run_intcode(codes)
print("------")
print(f"noun: {noun}, verb: {verb}")
print(f"--> output: {result[0]}")
print(f"answer: {100 * noun + verb}")
print("------")
