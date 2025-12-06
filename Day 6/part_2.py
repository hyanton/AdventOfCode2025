def main():
    def sum(matrix, index):
        total = 0
        for j in range(len(matrix) - 1):
            total += matrix[j][index]
        return total

    def multiply(matrix, index):
        total = 1
        for j in range(len(matrix) - 1):
            total *= matrix[j][index]
        return total

    with open('data.txt') as f:
        matrix = []
        for line in f.readlines():
            num = 0
            numbers = []
            for c in line:
                if c == ' ':
                    if num > 0:
                        numbers.append(num)
                        num = 0
                elif c == '+' or c == '*':
                    numbers.append(c)
                elif  c == '\n':
                    if num > 0:
                        numbers.append(num)
                    break
                else:
                    num = num * 10 + int(c)

            matrix.append(numbers)

        result = 0
        for index, operation in enumerate(matrix[-1]):
            if operation == '+':
                result += sum(matrix, index)
            else:
                result += multiply(matrix, index)

        print(f'Solution: {result}')


if __name__ == '__main__':
    main()
