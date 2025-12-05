def main():
    with open('example.txt') as f:
        intervals = set()
        read_intervals = True
        fresh_ingredients = 0
        i = 0
        for line in f.readlines():
            if line == '\n':
                read_intervals = False
                continue

            line = line.replace('\n', '')
            if read_intervals:
                line = line.split('-')
                low = int(line[0])
                high = int(line[1])
                for num in range(low, high + 1):
                    intervals.add(num)
            else:
                fresh_ingredients += bool(int(line) in intervals)

        print(f'Solution: {fresh_ingredients}')
if __name__ == '__main__':
    main()