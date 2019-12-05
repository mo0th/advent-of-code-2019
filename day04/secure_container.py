bounds = (172930, 683082)
passwords = []


def are_digits_increasing(num):
    num_string = str(num)
    return num_string == ''.join(sorted(num_string))


def has_double(num):
    num_string = str(num)
    for char in num_string:
        # change `>=` to `==` for part 2
        if num_string.count(char) >= 2:
            return True

    return False


for number in range(bounds[0], bounds[1] + 1):
    if are_digits_increasing(number) and has_double(number):
        passwords.append(number)

print("Answer:", len(passwords))
