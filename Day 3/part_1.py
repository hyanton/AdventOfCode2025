def main():
    with open('data.txt') as f:
        total_joltage = 0

        for line in f.readlines():
            line = line.replace('\n', '')
            digit_1 = 0
            digit_2 = 0

            i = 0
            while i < len(line) - 1:
                number = int(line[i])
                if number > digit_1:
                    digit_1 = number
                    digit_2 = 0
                elif number > digit_2:
                    digit_2 = number
                i += 1

            if int(line[-1]) > digit_2:
                digit_2 = int(line[-1])

            total_joltage += digit_1 * 10 + digit_2

        print(f'Solution: {total_joltage}')

if __name__ == '__main__':
    main()