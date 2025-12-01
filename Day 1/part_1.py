def main():
    with open('data.txt') as f:
        dial = 50
        code = 0

        for line in f.readlines():
            direction = -1 if line[0] == 'L' else 1
            rotation = int(line[1:])
            dial = (dial + direction * rotation) % 100

            if dial == 0:
                code += 1


        print(code)


if __name__ == '__main__':
    main()