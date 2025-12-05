def main():
    with open('data.txt') as f:
        intervals = []
        read_intervals = True
        fresh_ingredients = 0
        for line in f.readlines():
            if line == '\n':
                read_intervals = False
                continue

            line = line.replace('\n', '')
            if read_intervals:
                line = line.split('-')
                intervals.append([int(line[0]), int(line[1])])
            else:
                for interval in intervals:
                    if interval[0] <= int(line) <= interval[1]:
                        fresh_ingredients += 1
                        break

        print(f'Solution: {fresh_ingredients}')
if __name__ == '__main__':
    main()