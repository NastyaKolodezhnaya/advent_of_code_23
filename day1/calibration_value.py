from test_params import read_task


def make_calibration_value(arr: list[str]) -> int:
    res_ = []
    for line in arr:
        res = ''
        for letter in line:
            if letter.isdigit():
                res += letter

        res_.append(int(res[0] + res[-1]))

    return sum(res_)


# second star - not achieved ((
valid_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def make_calibration_value2(arr: list[str]) -> int:
    res_ = []
    for line in arr:
        line = line.strip()

        # first num
        word = ''
        for letter in line:
            if letter.isdigit():
                first = letter
                break

            word += letter  # fixme: nfour -> RFIND() for indecex
            if any(k for k in valid_digits if k.startswith(word)):
                if word in valid_digits:
                    first = valid_digits[word]
                    break
            else:
                word = ''

        # last num
        word = ''
        for letter in line[::-1]:
            if letter.isdigit():
                last = letter
                break

            word = letter + word
            if any(k for k in valid_digits if k.endswith(word)):
                if word in valid_digits:
                    last = valid_digits[word]
                    break
            else:
                word = ''

        res_.append(int(first + last))

        first = ''
        last = ''

    return sum(res_)


if __name__ == '__main__':
    input = read_task('day1/input.txt')
    print(make_calibration_value(input))
    # print(make_calibration_value2(input))
