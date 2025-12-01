def main():
    with open('data.txt') as f:
        dial = 50
        code = 0

        for line in f.readlines():
            dial_at_zero = dial == 0
            direction = -1 if line[0] == 'L' else 1
            rotation = int(line[1:])

            complete_rotation = rotation // 100
            code += complete_rotation

            small_rotation = rotation % 100

            temp_dial = dial + direction * small_rotation
            dial = temp_dial % 100

            if dial == 0:
                code += 1

            if temp_dial != dial and temp_dial % 100 != 0:
                code += 1
                if dial_at_zero:
                    code -= 1

        print(code)


if __name__ == '__main__':
    main()