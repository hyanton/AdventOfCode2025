def main():
    def multiply(l):
        total = 1
        for n in l:
            total *= n
        return total

    with open('data.txt') as f:
        matrix = []
        max_length = 0
        num_lines = 0

        for line in f.readlines():
            line = line.replace('\n', '')
            max_length = max(max_length, len(line))
            matrix.append(list(line))
            num_lines += 1

        for row in matrix:
            if len(row) < max_length:
                row.extend([' '] * (max_length - len(row)))

        result = 0
        numbers = []
        col = max_length - 1
        while col >= 0:
            number = 0
            for row in range(num_lines - 1):
                if matrix[row][col] == ' ':
                    continue
                else:
                    number = number * 10 + int(matrix[row][col])

            if matrix[-1][col] == ' ':
                numbers.append(number)
                col -= 1
            elif matrix[-1][col] == '+':
                numbers.append(number)
                result += sum(numbers)
                numbers = []
                col -= 2
            else:
                numbers.append(number)
                result += multiply(numbers)
                numbers = []
                col -= 2



        print(f'Solution: {result}')


if __name__ == '__main__':
    main()
