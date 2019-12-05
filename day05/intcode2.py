def get_program():
    # return [pad_num(i) for i in [1002, 4, 3, 4, 33]]
    with open('input.txt', 'r') as f:
        return [int(i) for i in f.readline().split(',')]


def get_opcode(code):
    return int(str(code).rjust(5, '0')[-2:])


def get_modes(code):
    mode_str = str(code).rjust(5, '0')[:3]
    return tuple(map(int, mode_str))


codes = get_program()
num_opcode_params = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    99: 0
}

print(codes)

i = 0
while i < len(codes):
    code = codes[i]
    opcode = get_opcode(code)
    # print("opcode:", opcode)
    modes = get_modes(code)
    if opcode == 99:
        break
    elif opcode not in num_opcode_params:
        continue
    num_params = num_opcode_params.get(opcode)
    instruction = codes[i:i+num_params]
    # print("code:", code)
    # print("instruction:", instruction)
    jumped = False

    if opcode in [1, 2, 5, 6, 7, 8]:
        num1 = codes[i + 1]
        if modes[2] == 0:
            num1 = codes[num1]
        num2 = codes[i + 2]
        if modes[1] == 0:
            num2 = codes[num2]
        dest_index = i if opcode == 5 and opcode == 6 else codes[i + 3]

        if opcode == 1:
            codes[dest_index] = num1 + num2
        elif opcode == 2:
            codes[dest_index] = num1 * num2
        elif opcode == 5:
            if num1 != 0:
                jumped = True
                i = num2
        elif opcode == 6:
            if num1 == 0:
                jumped = True
                i = num2
        elif opcode == 7:
            codes[dest_index] = 1 if num1 < num2 else 0
        elif opcode == 8:
            codes[dest_index] = 1 if num1 == num2 else 0

    elif opcode == 3:
        dest_index = codes[i + 1]
        codes[dest_index] = int(
            input("System ID (Part One: 1, Part Two: 5): "))

    elif opcode == 4:
        dest_index = codes[i + 1]
        print("output:", codes[dest_index])

    if not jumped:
        i += num_opcode_params[opcode]

# print(codes)
