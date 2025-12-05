def main():
    with open('example.txt') as f:
        fresh_ids = set()
        read_intervals = True

        for line in f.readlines():
            if line == '\n':
                read_intervals = False
                continue

            line = line.replace('\n', '')
            if read_intervals:
                line = line.split('-')
                low = int(line[0])
                high = int(line[1])
                fresh_ids = fresh_ids.union({x for x in range(low, high+1)})

        print(f'Solution: {len(fresh_ids)}')
if __name__ == '__main__':
    main()