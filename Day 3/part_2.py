def first_max_index(number: str, start:int, end: int) -> int:
    max_value = 0
    max_index = -1
    index = start

    while index <= end and max_value < 9:
        if int(number[index]) > max_value:
            max_index = index
            max_value = int(number[index])
        index += 1

    return max_index

def main():
    with open('data.txt') as f:
        total_joltage = 0

        for line in f.readlines():
            line = line.replace('\n', '')
            joltage = 0
            n = len(line)
            remaining = 12
            last_index = 0

            while remaining > 0:
                max_index = first_max_index(line, last_index, n - remaining)
                joltage = joltage * 10 + int(line[max_index])
                last_index = max_index + 1
                remaining -= 1

            total_joltage += joltage

        print(f'Solution: {total_joltage}')

if __name__ == '__main__':
    main()